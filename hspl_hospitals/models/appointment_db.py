from odoo import api, fields, models

class AppointmentDb(models.Model):
    _name = 'hspl.hospital.appointment'
    _description = 'appointments'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_id'

    booking_date = fields.Date(string='Booking Date', required=True, default=lambda s: fields.Date.context_today(s), tracking=True)
    patient_id = fields.Many2one('hspl.hospital.data', string="Patient", required=True, tracking=True)
    gender = fields.Selection(related='patient_id.gender')
    appointment_date = fields.Datetime(string='Appointment Date', required=True, tracking=True)
    ref = fields.Char('Ref', required=True, tracking=True, related='patient_id.ref')
    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'),
                                 ('2', 'High'), ('3', 'Very High')],
                                default='1', required=True, string='Priority', tracking=True)
    status = fields.Selection([('draft', 'Draft'), ('in_consultation', 'In Consultation'),
                                 ('done', 'Done'), ('cancelled', 'Cancelled')],
                                default="draft", string='Status', required=True, tracking=True)
    prescription = fields.Html('Prescription')
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy lines')
    image = fields.Image(string='Image')

    def action_test(self):
        print("clicked on object button")
        return {
            'effect':{
                'fadeout':'slow',
                'message':'Click Succesfully',
                'type':'rainbow_man'
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.status = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.status = 'done'

    def action_cancel(self):
        action = self.env.ref('hspl_hospitals.action_cancel_appointment').read()[0]
        return action

    def action_draft(self):
        for rec in self:
            rec.status = 'draft'


class AppointmentPharmacylines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one('hspl.hospital.appointment', string='Appointment')