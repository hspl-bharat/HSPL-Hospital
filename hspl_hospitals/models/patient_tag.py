from odoo import api, fields, models

class PatientTag(models.Model):
    _name ='patient.tag'
    _description = 'Patient Tags'

    name = fields.Char('Name', required=True, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    color = fields.Text(string='color')
