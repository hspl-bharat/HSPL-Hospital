from odoo import api, fields, models
from datetime import date

class TestingDb(models.Model):
    _name ='hspl.hospital.data'
    _description = 'testing'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    date = fields.Datetime(string='Date', required=True, default=fields.Datetime.now, tracking=True)
    name = fields.Char('Name', required=True, tracking=True)
    date_of_birth = fields.Date('Date Of Birth', required=True, tracking=True)
    ref = fields.Char('Ref', required=True, tracking=True)
    age = fields.Integer('Age', compute='_compute_age')
    gender = fields.Selection([('M', 'Male'), ('F', 'Female')], required=True, string='Gender', tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    # prescription = fields.Html('Prescription')

    @api.depends('date_of_birth')
    def _compute_age(self):
        print(self)
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year - ((today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 0

