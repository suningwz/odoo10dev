# -*- coding: utf-8 -*-
from odoo import http

# class Scaffolddemo(http.Controller):
#     @http.route('/scaffolddemo/scaffolddemo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scaffolddemo/scaffolddemo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scaffolddemo.listing', {
#             'root': '/scaffolddemo/scaffolddemo',
#             'objects': http.request.env['scaffolddemo.scaffolddemo'].search([]),
#         })

#     @http.route('/scaffolddemo/scaffolddemo/objects/<model("scaffolddemo.scaffolddemo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scaffolddemo.object', {
#             'object': obj
#         })