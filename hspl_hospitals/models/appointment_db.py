from odoo import api, fields, models, _


class AppointmentDb(models.Model):
    _name = 'hspl.hospital.appointment'
    _description = 'appointments'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_name'

    appointment_id = fields.Char('ID')
    booking_date = fields.Date(string='Booking Date', required=True, default=lambda s: fields.Date.context_today(s),
                               tracking=True)
    # patient_name_tree_view = fields.Char(related='patient_name.name', string='Patient')
    patient_name = fields.Many2one('hspl.hospital.data', string="Patient", required=True, tracking=True)
    gender = fields.Selection(related='patient_name.gender')
    appointment_date = fields.Datetime(string='Appointment Date', required=True, tracking=True)
    ref = fields.Char('Ref', required=True, tracking=True, related='patient_name.ref')
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
    cancel_reason = fields.Text(string='Reason')
    pending_appointment = fields.Integer('Pending Appointment', compute='_compute_pending_appointment')

    def action_test(self):
        print("clicked on object button")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Succesfully',
                'type': 'rainbow_man'
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

    @api.depends('status')
    def _compute_pending_appointment(self):
        total_len = self.env['hspl.hospital.appointment'].search_count([('status', '=', 'draft')])
        self.pending_appointment = total_len

    def action_pending_appointment_view(self):
        return {
            'name': 'draft_view',
            'view_mode': 'tree,form',
            'domain': [('status', 'in', ['draft'])],
            'res_model': 'hspl.hospital.appointment',
            'type': 'ir.actions.act_window',
        }

    @api.model
    def create(self, values):
        values['appointment_id'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(AppointmentDb, self).create(values)

    def write(self, values):
        if not self.appointment_id and not values.get('appointment_id'):
            values['appointment_id'] = self.env['ir.sequence'].next_by_code('patient.appointment')
        return super(AppointmentDb, self).write(values)

    # @api.model
    # def get_view(self, view_id=None, view_type='form', **options):
    #     if view_type == 'form':
    #         self.with_context(get_sizes=True)
    #     return super().get_view(view_id, view_type, **options)


    # @api.model
    # def get_view(self, view_id=None, view_type='form'):
    #     if view_type == 'form':
    #         return {
    #             'type': 'ir.actions.act_window',
    #             'name': self.name,
    #             'res_model': 'hspl.hospital.appointment',
    #             'res_id': self.id,
    #             'view_mode': 'form',
    #             'view_id': view_id,
    #         }
    #     elif view_type == 'tree':
    #         return {
    #             'type': 'ir.actions.act_window',
    #             'name': self.name,
    #             'res_model': 'hspl.hospital.appointment',
    #             'view_mode': 'tree',
    #             'view_id': view_id,
    #         }
    #     else:
    #         return super(AppointmentDb, self).get_view(view_id=view_id, view_type=view_type)


class AppointmentPharmacylines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one('hspl.hospital.appointment', string='Appointment')
