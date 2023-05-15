# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    cancel_appointment_days = fields.Integer(string="Cancel Days", config_parameter="hspl_hospitals.cancel_appointment_days")
    hospital_email = fields.Char(string='Email Id', config_parameter="hspl_hospitals.hospital_email")
    hospital_contact = fields.Char('Hospital Contact', config_parameter="hspl_hospitals.hospital_contact")