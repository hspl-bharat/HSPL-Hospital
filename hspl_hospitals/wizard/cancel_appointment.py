import datetime
from odoo import api, fields, models

class CancelAppointmentWizard(models.TransientModel):
    _name ='cancel.appointment.wizard'
    _description = 'Appointment Cancellation Wizard'

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        return res

    appointment_id = fields.Many2one('hspl.hospital.appointment', string="Appointment")
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string='Cancellation Date')
    state = fields.Selection(related="appointment_id.status")



    def action_cancel(self):
        self.appointment_id.cancel_reason = self.reason if self.reason else ''
        self.appointment_id.status = 'cancelled'
