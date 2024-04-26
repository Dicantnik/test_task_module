from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Route(models.Model):
    _name = 'test.route'

    route_number = fields.Char(
        string='Number',
        required='True'
    )
    car_id = fields.Many2one(
        'test.car',
        string='Car'
    )
    carrier_id = fields.Many2one(
        'res.partner',
        related='car_id.carrier_id',
        required='True'
    )
    order_ids = fields.Many2many(
        'test.order',
        string='Orders',
        required='True'
    )

    @api.constrains('car_id', 'order_ids')
    def _check_weight_volume(self):
        current_weight = 0
        current_volume = 0
        for order in self.order_ids:
            current_weight += order.order_weight
            current_volume += order.order_volume
        if self.car_id.max_weight < current_weight:
            raise ValidationError('Weight more than car can transport')
        if self.car_id.max_volume < current_volume:
            raise ValidationError('Volume more than car can transport')

    _sql_constraints = [('unique_number',
                         'unique (route_number)',
                         'Number must be unique')]
