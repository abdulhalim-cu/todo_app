# -*- coding: utf-8 -*-
from odoo import http

# class TodoUser(http.Controller):
#     @http.route('/todo_user/todo_user/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_user/todo_user/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_user.listing', {
#             'root': '/todo_user/todo_user',
#             'objects': http.request.env['todo_user.todo_user'].search([]),
#         })

#     @http.route('/todo_user/todo_user/objects/<model("todo_user.todo_user"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_user.object', {
#             'object': obj
#         })