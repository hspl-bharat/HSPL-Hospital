from odoo import api, fields, models, _


class ResPartner(models.Model):
    _name = 'res.partner.inherit'
    _inherits = {"res.partner": 'partner_id'}

    partner_id = fields.Many2one('res.partner', string='res_partner_inherit')