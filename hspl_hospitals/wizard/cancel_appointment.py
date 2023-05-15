import datetime
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from dateutil import relativedelta
from datetime import date

class CancelAppointmentWizard(models.TransientModel):
    _name ='cancel.appointment.wizard'
    _description = 'Appointment Cancellation Wizard'

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        # if self.env.context.get('active_id'):        ## python method to use active_id in xml
        #     res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('hspl.hospital.appointment', string="Appointment")
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string='Cancellation Date')
    state = fields.Selection(related="appointment_id.status")



    def action_cancel(self):
        cancel_days = self.env['ir.config_parameter'].get_param('hspl_hospitals.cancel_appointment_days')
        allowed_date = self.appointment_id.appointment_date - relativedelta.relativedelta(days=int(cancel_days))
        print(">>>>>>>>>>>>>>>>>>>>>>", allowed_date)
        print(">>>>>>>>>>>>>>>>>>>>>>", datetime.datetime.today())
        if allowed_date < datetime.datetime.today():
            raise ValidationError(_("Sorry, Cancellation is not allowed according to given cancellation policy"))
        if self.appointment_id.appointment_date.date() == fields.Date.today():
            raise ValidationError(_("Sorry, Cancellation is not allowed on the day of Appointment day"))
        self.appointment_id.cancel_reason = self.reason if self.reason else ''
        self.appointment_id.status = 'cancelled'
        return {
            'type' : 'ir.actions.client',
            'tag' : 'reload'
        }


