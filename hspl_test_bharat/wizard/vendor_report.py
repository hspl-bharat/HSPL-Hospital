from odoo import api, fields, models, _
import xlsxwriter
from io import BytesIO

class AppointmentReportWizard(models.TransientModel):
    _name ='vendor.report.wizard'
    _description = 'Vendor Report Wizard'

    vendor_ids = fields.Many2many('res.partner', string="Vendor Id")



    def action_print_vendor_report(self):
        purchase_obj = self.env['purchase.order']
        for vender_id in self.vendor_ids:
            purchase_ids = purchase_obj.search([('partner_id', '=', vender_id.id)])
        if purchase_ids:
            file_data = BytesIO()
            workbook = xlsxwriter.Workbook(file_data)
            worksheet = workbook.add_worksheet()
        headers = [
            "PO #",
            "Date",
            "Vendor Name",
            "Status",
            "Total Amount"
        ]

        sheet = workbook.add_worksheet("Vendor Report")
        bold = workbook.add_format({"bold": True})
        date_format = workbook.add_format(
            {"text_wrap": True, "num_format": "dd-mm-yyyy"}
        )
        row = 0
        column = 0
        for header in headers:
            sheet.set_column(row, column, 19)
            sheet.write(row, column, header, bold)
            column = column + 1

        row = 1
        i = 0
        for rec in purchase_ids:
            column = 0
            sheet.write(row, column, rec.name or "")
            column = column + 1
            sheet.write(row, column, rec.date_order, date_format)
            column = column + 1
            sheet.write(row, column, rec.partner_id.name or "")
            column = column + 1
            sheet.write(row, column, rec.state or "")
            column = column + 1
            sheet.write(row, column, rec.amount_total or "")
            column = column + 1
            row = row + 1
            i = i + 1
        print("----------------hiiiiiiiiiiiiiii")