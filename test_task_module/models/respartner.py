from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_group = fields.Selection([
        ('client', 'Client'),
        ('supplier', 'Supplier'),
        ('carrier', 'Carrier')],
        string='Group of Partner',
        default='client'  # Set the default value to one of the choices
    )
