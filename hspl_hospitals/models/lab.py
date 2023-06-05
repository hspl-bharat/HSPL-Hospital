from odoo import api, fields, models, _


class HospitalLab(models.Model):
    _name = 'hspl.hospital.lab'
    _description = 'Hospital Laboratory'

    name = fields.Char('Name', required=True)
    user_id = fields.Many2one('res.users', string='Responsible')