from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Order(models.Model):
    _name = 'test.order'

    name = fields.Char(
        string='Name Order',
        required='True'
    )
    order_date = fields.Date(
        default=fields.Date.today,
        string='Date',
        readonly='True'
    )
    client_id = fields.Many2one(
        'res.partner',
        string='Client',
        required='True'
    )
    supplier_id = fields.Many2one(
        'res.partner',
        string='Supplier',
        required='True'
    )
    order_cost = fields.Float(
        string='Cost',
        readonly='True',
        compute='_compute_cost'
    )
    order_weight = fields.Float(
        string='Weight',
        readonly='True',
        compute='_compute_weight'
    )
    order_volume = fields.Float(
        string='Volume',
        readonly='True',
        compute='_compute_volume'
    )
    order_line_ids = fields.One2many(
        'test.orderline',
        'order_id',
        string='OrderLine',
        required='True'
    )

    @api.constrains('client_id')
    def _check_on_client(self):
        if self.client_id.partner_group != 'client':
            raise ValidationError('On field Client must be person(client)')

    @api.constrains('supplier_id')
    def _check_on_supplier(self):
        if self.supplier_id.partner_group != 'supplier':
            raise ValidationError('On field Supplier must be person(supplier)')

    @api.depends('order_line_ids')
    def _compute_cost(self):
        for order in self:
            cost = 0
            for orderline in order.order_line_ids:
                cost += orderline.cost
            order.order_cost = cost

    @api.depends('order_line_ids')
    def _compute_weight(self):
        for order in self:
            weight = 0
            for orderline in order.order_line_ids:
                weight += orderline.product_id.weight * orderline.count
            order.order_weight = weight

    @api.depends('order_line_ids')
    def _compute_volume(self):
        for order in self:
            volume = 0
            for orderline in order.order_line_ids:
                volume += orderline.product_id.volume * orderline.count
            order.order_volume = volume
