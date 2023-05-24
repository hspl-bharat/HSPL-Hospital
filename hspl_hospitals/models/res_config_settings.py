# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']
    _description = 'Data releted to settings like hospital email, contact, abouts, etc'


    cancel_appointment_days = fields.Integer(string="Cancel Days", config_parameter="hspl_hospitals.cancel_appointment_days")
    hospital_email = fields.Char(string='Email Id', config_parameter="hspl_hospitals.hospital_email")
    hospital_contact = fields.Char('Hospital Contact', config_parameter="hspl_hospitals.hospital_contact")