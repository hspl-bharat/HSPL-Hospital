from odoo import http
from odoo.http import request

class WebView(http.Controller):

    @http.route(['/home'], type='http', auth='public', website=True)
    def home(self):
        patients = request.env['hspl.hospital.data'].search([])
        print('>>>>>>>>>>>>>',patients)
        values = {
            'patients':patients
        }
        # return "hello"
        return request.render('hspl_hospitals.patients_controller_view', values)
