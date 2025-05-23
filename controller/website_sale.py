# -*- coding: utf-8 -*-
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class WebsiteSaleCustom(WebsiteSale):
    def _shop_lookup_products(self, attrib_set, options, post, search, website):
        """show only allowed products on the shop based on logged user """
        fuzzy_search_term, product_count, search_result = (super()._shop_lookup_products
                                                           (attrib_set, options, post, search, website))
        user = request.env.user
        partner = user.partner_id
        if partner.allowed_products == 'product' and partner.product_ids:
            search_result = search_result.filtered(lambda p: p.id in partner.product_ids.ids)
        elif partner.allowed_products == 'product_categories' and partner.product_category_ids:
            search_result = search_result.filtered(lambda p: p.categ_id.id in partner.product_category_ids.ids)
        return fuzzy_search_term, len(search_result), search_result




