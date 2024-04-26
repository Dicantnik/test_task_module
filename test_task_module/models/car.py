from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Car(models.Model):
    _name = 'test.car'

    car_number = fields.Char(
        string='Car Number',
        required='True'
    )
    carrier_id = fields.Many2one(
        'res.partner',
        required='True'
    )
    max_weight = fields.Float(
        string='Max Weight',
        required='True'
    )
    max_volume = fields.Float(
        string='Max Volume',
        required='True'
    )

    @api.constrains('carrier_id')
    def _check_on_carrier(self):
        if self.carrier_id.partner_group != 'carrier':
            raise ValidationError('This person must be carrier')

    _sql_constraints = [(
        'unique_car_number',
        'unique (car_number)',
        'Car Number must be unique')]
