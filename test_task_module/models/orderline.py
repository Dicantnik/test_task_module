from odoo import models, fields, api
from odoo.exceptions import ValidationError


class OrderLine(models.Model):
    _name = 'test.orderline'

    order_id = fields.Many2one(
        'test.order',
        string='Order'
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required='True'
    )
    price = fields.Float(
        related='product_id.lst_price',
        string='Price'
    )
    count = fields.Float(
        string='Count',
        default=1,
        required='True'
    )
    cost = fields.Float(
        string='Cost',
        readonly='True',
        compute='_compute_cost'
    )

    @api.constrains('count')
    def _check_count(self):
        if self.count <= 0:
            raise ValidationError('Count can`t be <= 0')

    @api.depends('price', 'count')
    def _compute_cost(self):
        for orderline in self:
            orderline.cost = orderline.count * orderline.price

    @api.constrains('order_id', 'product_id')
    def _check_unique_product(self):
        for order_line in self:
            if self.env['test.orderline'].search_count([('order_id', '=', order_line.order_id.id), ('product_id', '=', order_line.product_id.id)]) > 1:
                raise ValidationError('You cannot add the same product more than once in an order.')
