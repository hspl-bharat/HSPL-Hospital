from odoo import api, fields, models

class CancelAppointmentWizard(models.TransientModel):
    _name ='cancel.appointment.wizard'
    _description = 'Appointment Cancellation Wizard'

    appointment_id = fields.Many2one('hspl.hospital.appointment', string="Appointment")
    reason  = fields.Text(string="Reason")

    def action_cancel(self):
        for rec in self:
            rec.status = 'cancelled'