# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)


class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    _description = "To-Do Mass Assignment"
    task_ids = fields.Many2many('todo.task', string="Tasks")
    new_deadline = fields.Date('Deadline to set')
    new_user_id = fields.Many2one('res.users', string="Responsible to set")

    @api.multi
    def do_mass_update(self):
        self.ensure_one()
        if not (self.new_deadline or self.new_user_id):
            raise exceptions.ValiationError('No data to update!')
        _logger.debug("Mass update on Todo Tasks %s", self.task_ids.ids)

        vals = {}
        if self.new_deadline:
            vals['date_deadline'] = self.new_deadline
        if self.new_user_id:
            vals['user_id'] = self.new_user_id

        # Mass write values on all selected tasks
        if vals:
            self.task_ids.write(vals)
        return True

    @api.multi
    def do_count_tasks(self):
        Task = self.env['todo.task']
        count = Task.search_count([('is_done', '=', False)])
        raise exceptions.Warning('There are %d active tasks.' % count)

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        return {
                'type': 'ir.actions.act_window',
                'res_model': self._name,    # this model
                'res_id': self.id,          # the current wizard record
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new'
                }

    @api.multi
    def do_populate_tasks(self):
        import pdb
        pdb.set_trace()
        self.ensure_one()
        Task = self.env['todo.task']
        open_tasks = Task.search([('is_done', '=', False)])
        # Fill the wizard task list with all tasks
        self.task_ids = open_tasks          # all_tasks
        # reopen wizard form on same wizard record
        return self._reopen_form()
