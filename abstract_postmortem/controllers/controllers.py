# -*- coding: utf-8 -*-
# from odoo import http


# class AbstractPostmortem(http.Controller):
#     @http.route('/abstract_postmortem/abstract_postmortem', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abstract_postmortem/abstract_postmortem/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abstract_postmortem.listing', {
#             'root': '/abstract_postmortem/abstract_postmortem',
#             'objects': http.request.env['abstract_postmortem.abstract_postmortem'].search([]),
#         })

#     @http.route('/abstract_postmortem/abstract_postmortem/objects/<model("abstract_postmortem.abstract_postmortem"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abstract_postmortem.object', {
#             'object': obj
#         })
