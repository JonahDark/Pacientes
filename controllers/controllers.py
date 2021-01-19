# -*- coding: utf-8 -*-
# from odoo import http


# class PacientesApp(http.Controller):
#     @http.route('/pacientes_app/pacientes_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pacientes_app/pacientes_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pacientes_app.listing', {
#             'root': '/pacientes_app/pacientes_app',
#             'objects': http.request.env['pacientes_app.pacientes_app'].search([]),
#         })

#     @http.route('/pacientes_app/pacientes_app/objects/<model("pacientes_app.pacientes_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pacientes_app.object', {
#             'object': obj
#         })
