from odoo import models, fields


class Product(models.Model):
    _inherit = 'product.product'

    weight = fields.Float(
        string='weight',
        default=10.0
    )
    volume = fields.Float(
        string='volume',
        default=10.0
    )
