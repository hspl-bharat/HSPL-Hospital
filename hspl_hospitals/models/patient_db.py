from odoo import api, fields, models
from datetime import date

class HosptialPatient(models.Model):
    _name ='hspl.hospital.data'
    _description = 'testing'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Char('ID')
    date = fields.Datetime(string='Date', required=True, default=fields.Datetime.now, tracking=True)
    name = fields.Char('Name', required=True, tracking=True)
    date_of_birth = fields.Date('Date Of Birth', required=True, tracking=True)
    ref = fields.Char('Ref', required=True, tracking=True)
    age = fields.Integer('Age', compute='_compute_age')
    gender = fields.Selection([('M', 'Male'), ('F', 'Female')], required=True, string='Gender', tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    # prescription = fields.Html('Prescription')

    @api.model
    def create(self, values):
        values['patient_id'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HosptialPatient, self).create(values)

    def write(self, values):
        if not self.patient_id and not values.get('patient_id'):
            values['patient_id'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HosptialPatient, self).write(values)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year - ((today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 0

    def name_get(self):
        patient_lst = []
        for rec in self:
            name = rec.name + '  ' + '[' + rec.ref + ']'
            patient_lst.append((rec.id, name))
        return patient_lst
    # return [(rec.id, "%s:%s" % (rec.name, rec.ref )) for rec in self]
