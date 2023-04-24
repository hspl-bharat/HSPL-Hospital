# -*- coding: utf-8 -*-
# from odoo import http


# class HsplHospitalInheritance(http.Controller):
#     @http.route('/hspl_hospital_inheritance/hspl_hospital_inheritance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hspl_hospital_inheritance/hspl_hospital_inheritance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hspl_hospital_inheritance.listing', {
#             'root': '/hspl_hospital_inheritance/hspl_hospital_inheritance',
#             'objects': http.request.env['hspl_hospital_inheritance.hspl_hospital_inheritance'].search([]),
#         })

#     @http.route('/hspl_hospital_inheritance/hspl_hospital_inheritance/objects/<model("hspl_hospital_inheritance.hspl_hospital_inheritance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hspl_hospital_inheritance.object', {
#             'object': obj
#         })
