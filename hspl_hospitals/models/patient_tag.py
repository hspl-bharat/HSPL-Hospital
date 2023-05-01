from odoo import api, fields, models

class PatientTag(models.Model):
    _name ='patient.tag'
    _description = 'Patient Tags'

    name = fields.Char('Name', required=True, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    color = fields.Text(string='color')
    sequence = fields.Integer(string='Sequence')

    _sql_constraints = [
        ('unique_tag_name', 'unique (name,active)', 'Name and Fields must be unique.'),
        ('unique_tag_name', 'unique (sequence)', 'Sequence must be unique.'),
        ('check_sequence_number', 'check (sequence > 0)', 'Sequence must be grater than zero')
    ]