from odoo import fields,models


class ResPartner(models.Model):
    """add a selection field to the inherited form view of res.partner"""
    _inherit = "res.partner"
    _description = "res partner"


    allowed_products = fields.Selection(string='Allowed Products',
                              selection=[('product', 'Product'),
                                         ('product_categories', 'Product Categories '),], )
    product_ids = fields.Many2many('product.template' , 'product_product_res_partner_rel','res_partner_id', 'product_product_id', string="Product")
    product_category_ids = fields.Many2many('product.category', 'product_category_res_partner_rel', 'res_partner_id', 'product_category_id', string='Product Category')