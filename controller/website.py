from odoo import models

class Website(models.Model):
    _inherit = 'website'

    def _search_render_results(self, search_details, limit):
        search_details = super()._search_render_results(search_details, limit)

        partner = self.env.user.partner_id
        allowed_type = partner.allowed_products
        allowed_product_ids = set(partner.product_ids.ids)
        allowed_category_ids = set(partner.product_category_ids.ids)

        for search_detail in search_details:
            model_name = search_detail['model']
            results_data = search_detail.get('results_data', [])

            if model_name == 'product.template':
                if allowed_type == 'product':
                    results_data = [
                        item for item in results_data
                        if item.get('id') in allowed_product_ids
                    ]
            elif model_name == 'product.public.category':
                if allowed_type == 'product':
                    results_data = []
                if allowed_type == 'product_categories':
                    results_data = [
                        item for item in results_data
                        if item.get('id') in allowed_category_ids
                    ]
            search_detail['results_data'] = results_data
        return search_details
