
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class TodoTask(models.Model):
    _name='todo.task'
    _description='todo.task model'
    
    name = fields.Char(
        string=u'Description',
    )
    date_deadline = fields.Date(
        string=u'Deadline',
        default=fields.Date.context_today,
    )
    is_done = fields.Boolean(
        string=u'Done?',
    ) 
    active = fields.Boolean(
        string=u'Active',
        default=True,
    )
    user_id = fields.Many2one(
        string=u'Responsible',
        comodel_name='res.users',
        ondelete='set null',
    )
    refer_to = fields.Reference(
        string=u'Refer To',
        selection=[('res.users', 'User'),('res.partner', 'Partner')]
    )
    stage_id = fields.Many2one(
        string=u'Stage',
        comodel_name='todo.task.stage',
        ondelete='set null',
    )
    stage_state = fields.Selection(
        string=u'Stage State',        
        related='stage_id.state',        
    )
    
    tag_ids = fields.Many2many(
        string=u'Tags',
        comodel_name='todo.task.tag',
    )


class Stage(models.Model):
    _name='todo.task.stage'
    desc = fields.Text(
        string=u'Description',
    )
    docs = fields.Html(
        string=u'Documentation',
    )
    sequence = fields.Integer(
        string=u'Sequence',
    )
    state = fields.Selection(
        string=u'State',
        selection=[('draft', 'New'), ('open', 'Started'),('done','Closed')]
    )
    fold = fields.Boolean(
        string=u'Folded?',
    )
    date_effective = fields.Date(
        string=u'Effective Date',
    )
    date_changed = fields.Datetime(
        string=u'Last Changed',
        default=fields.Datetime.now,
    )
    image = fields.Binary(
        string=u'Image',
    )


class Tag(models.Model):
    _name='todo.task.tag'
    _parent_store = True
    
    parent_left = fields.Integer('Left Parent', index=1)
    parent_right = fields.Integer('Right Parent', index=1)
    
        
    name = fields.Char(
        string=u'Name',
    )
    parent_id = fields.Many2one(
        string=u'Parent Tag',
        comodel_name='todo.task.tag',
        ondelete='restrict',
    )

    
    
    
    
    
    
    
    
    
    
    
    


    
    
    
    
    
    
    
    