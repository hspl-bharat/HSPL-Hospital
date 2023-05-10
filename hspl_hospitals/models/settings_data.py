from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError

class HospitalSettings(models.Model):
    _name = 'hspl.hospital.settings'
    _description = 'Data releted to settings like hospital email, contact, abouts, etc'

    hospital_email = fields.Char('Email')
    hospital_contact = fields.Integer('Contacts')

