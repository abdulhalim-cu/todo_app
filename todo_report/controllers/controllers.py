# -*- coding: utf-8 -*-
from odoo import http

# class TodoReport(http.Controller):
#     @http.route('/todo_report/todo_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_report/todo_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_report.listing', {
#             'root': '/todo_report/todo_report',
#             'objects': http.request.env['todo_report.todo_report'].search([]),
#         })

#     @http.route('/todo_report/todo_report/objects/<model("todo_report.todo_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_report.object', {
#             'object': obj
#         })