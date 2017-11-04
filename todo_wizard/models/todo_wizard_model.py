# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TodoWizard(model.TransientModel):
    _name = 'todo.wizard'
    _description="To-Do Mass Assignment"
    task_ids = fields.Many2many('todo.task', string="Tasks")
    new_deadline = fields.Date('Deadline to set')
    new_user_id = fields.Many2one('res.users', string="Responsible to set")
