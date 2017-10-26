# -*- coding: utf-8 -*-
from odoo import http

# class Librarybook(http.Controller):
#     @http.route('/librarybook/librarybook/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/librarybook/librarybook/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('librarybook.listing', {
#             'root': '/librarybook/librarybook',
#             'objects': http.request.env['librarybook.librarybook'].search([]),
#         })

#     @http.route('/librarybook/librarybook/objects/<model("librarybook.librarybook"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('librarybook.object', {
#             'object': obj
#         })