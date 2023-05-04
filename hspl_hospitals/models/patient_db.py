from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
import smtplib


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
    email = fields.Char('Email')
    active = fields.Boolean('Active', default=True, tracking=True)
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    patient_appointment_id = fields.One2many('hspl.hospital.appointment', 'patient_name', string='Appointment_id')
    appointment_count = fields.Integer('Total Appointment', compute='_compute_appointment_count', store=False)
    # prescription = fields.Html('Prescription')

    @api.model
    def send_birthday_mail(self):
        # Query the database for people with birthdays today
        today = date.today().strftime('%m-%d')
        patientss = self.env['hspl.hospital.data'].search([('date_of_birth', 'like', today)])

        # Send emails to employees with birthdays
        for patient in patientss:
            email_to = patient.email
            email_subject = 'Happy Birthday {}'.format(patient.name)
            email_body = 'Happy birthday, {}!'.format(patient.name)

            # Send email using smtplib
            gmail_user = 'bharathsplb@gmail.com'
            gmail_password = 'Heliconia@1234'

            message = 'Subject: {}\n\n{}'.format(email_subject, email_body)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, email_to, message)
            server.quit()

    # @api.depends('patient_appointment_id')
    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hspl.hospital.appointment'].search_count([('patient_name', '=', rec.id)])
            rec.appointment_count = appointment_count
            # rec.appointment_count = len(rec.patient_appointment_id)
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The entered date of birth is not accepted"))
    @api.model
    def create(self, values):
        res = super(HosptialPatient, self).create(values)
        id = str(res.id)
        res.patient_id = self.env['ir.sequence'].next_by_code('hospital.patient') + id
        # print('VVVVVVVVVVV', res, res.id, res.read())
        return res

    def write(self, values):
        print(">>>>>>>>>>>>>>>", date.today().strftime('%m-%d'))
        print(">>>>>>>>>>>>>>>", self.date_of_birth.strftime('%m-%d'))
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
