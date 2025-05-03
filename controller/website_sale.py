from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route
from odoo import http

class WebsiteSaleCustom(WebsiteSale):
    @http.route([
           '/shop',
           '/shop/page/<int:page>',
           '/shop/category/<model("product.public.category"):category>',
          '/shop/category/<model("product.public.category"):category>/page/<int:page>',
       ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', **post):
        print("hi")
        result = super().shop(page=page, category=category, search=search, **post)

        user = request.env.user
        partner = user.partner_id

        domain = []
        if partner.product_ids:
            domain = [('id', 'in', partner.product_ids.ids)]
            print(partner.product_ids)
        elif partner.product_category_ids:
            domain = [('product_category_ids', 'in', partner.product_category_ids.ids)]

        if domain:
            filtered_products = request.env['product.template'].search(domain)
            print(result.qcontext['products'])
            result.qcontext['products'] = filtered_products
            print(result.qcontext['products'])

        return result