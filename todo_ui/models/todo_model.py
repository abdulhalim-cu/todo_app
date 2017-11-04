# -*- coding: utf-8 -*-

from odoo import models, fields, api
# from odoo.exceptions import ValidationError
# Import Referenceable models configuration to improve flaxibility of Refers to field
from odoo.addons.base.res.res_request import referenceable_models


class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'
    # Enable heirarchic relationship features 
    _parent_store = True
    name = fields.Char('Name')
    # _parent_name = 'parent_id'
    # Parent-child tree relationships using a Many2one relationships
    parent_id = fields.Many2one('todo.task.tag', 'Parent Tag', ondelete='restrict')
    parent_left = fields.Integer('Parent Left', index=True)
    parent_right = fields.Integer('Parent Right', index=True)


class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence,name'
    
    # String fields:
    name = fields.Char('Name')
    desc = fields.Text('Description')
    state = fields.Selection(
                [('draft', 'New'), ('open', 'Started'),
                 ('done', 'Closed')], 'State')
    docs = fields.Html('Documentation')

    # Numeric Fields:
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))

    # Date fields:
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')

    # other fields:
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')


class TodoTask(models.Model):
    _inherit = 'todo.task'
    
    # Refers to field that can either refer to a User or a Partner
    # refers_to = fields.Reference(
    #             [('res.user', 'User'), ('res.partner', 'Partner')], 'Refers to')
    # Modifying referenceable model configuration to extend flaxibility
    refers_to = fields.Reference(referenceable_models, 'Refers to')

    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    # Tasl <-> Tag relation (positional args)
    tag_ids = fields.Many2many('todo.task.tag',     # related model
                'todo_task_tags_rel',               # relation table name for avoiding limitations
                'task_id',                          # field for 'this' record
                'tag_id',                           # field for 'other' record
                string="Tags")
    # We can instead use keyword arguments, which some people prefer for readability
    # Task <-> Tag relation (keyword args)
    # tag_ids = fields.Many2many(
    #           comodel_name='todo.task.tag',       # related model
    #           relation='todo_task_tag_rel',       # relation table name for avoiding limitations
    #           column1='task_id',                  # field for 'this' record
    #           column2='tag_id',                   # field for 'other' record
    #           string='Tags')
    
    
    # Compute field declaration and set a search function for search logic
    # and inverse function for implementing write logic
    stage_fold = fields.Boolean(string='Stage Folded?', 
            compute='_compute_stage_fold',
            search = '_search_stage_fold',
            inverse = '_write_stage_fold')

    # Related fields for auto handle computed fields
    stage_state = fields.Selection(
                related='stage_id.state',
                string='Stage State'
            )

    # SQL constraints
    _sql_constraints = [('todo_task_name_uniq',
                    'UNIQUE (name, active)',
                    'Task title must be unique!')]
    # python constraints
    # @api.constrains('name')
    #  def _check_name_size(self):
    #      for todo in self:
    #          if len(todo.name) < 5:
    #              raise ValidationError('Must have 5 chars!')

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for task in self:
            task.stage_fold = task.stage_id.fold

    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold

    def compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count(
                        [('user_id', '=', task.user_id.id)]
                    )
    user_todo_count = fields.Integer('User To-Do Count', 
                compute='compute_user_todo_count'
            )

