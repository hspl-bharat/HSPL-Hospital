from odoo import api, fields, models, _
import xlwt
import base64
from io import BytesIO

class AppointmentReportWizard(models.TransientModel):
    _name ='appointment.report.wizard'
    _description = 'Appointment Report Wizard'

    patient_id = fields.Many2one('hspl.hospital.data', string="Appointment")
    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date')


    def action_print_pdf_report(self):
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_name', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('appointment_date', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('appointment_date', '<=', date_to)]
        appointments = self.env['hspl.hospital.appointment'].search_read(domain)
        print('----------',appointments)
        data = {
            'from_data': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('hspl_hospitals.action_qweb_report_appointment').report_action(self, data=data)

    def action_print_xlsx_report(self):
        filename = self.patient_id.name
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet1 = workbook.add_sheet('Appointments', cell_overwrite_ok=True)
        format1 = xlwt.easyxf('align: horiz center; font: color black,bold True; borders: top_color black, bottom_color black, left_color black, right_color black, left thin, right thin,top thin,bottom thin; pattern: pattern solid, fore_color aqua')

        sheet1.col(0).width = 7000
        sheet1.write(0,0,self.patient_id.name,format1)

        stream = BytesIO()
        workbook.save(stream)
        out = base64.encodebytes(stream.getvalue())
        print("Excel Report")
