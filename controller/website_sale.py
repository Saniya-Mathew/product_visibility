from odoo.addons.website_sale.controllers.main import WebsiteSale

from addons.website_sale.controllers.main import TableCompute
from odoo.http import request
from odoo import http
from odoo.tools import lazy
from odoo.addons.website_sale.controllers import main


class WebsiteSaleCustom(WebsiteSale):

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>',
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', **post):
        response = super(WebsiteSaleCustom, self).shop(page=page, category=category, search=search, **post)

        user = request.env.user
        partner = user.partner_id
        domain = []
        if partner.allowed_products == 'product' and partner.product_ids:
            domain = [('id', 'in', partner.product_ids.ids)]
            print(partner.product_ids.ids)
        elif partner.allowed_products == 'product_categories' and partner.product_category_ids:
            domain = [('categ_id', 'in', partner.product_category_ids.ids)]

        if domain:
            filtered_products = request.env['product.template'].search(domain)
            # response.qcontext['products'] = filtered_products
            response.qcontext['bins'] = lazy(lambda: TableCompute().process(filtered_products, ppg, ppr))
        return response