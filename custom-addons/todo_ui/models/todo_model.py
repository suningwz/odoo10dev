
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class TodoTask(models.Model):
    """ extend todo.task defined in todo_app

    Fields:
      name (Char): Human readable name which will identify each record.

    """

    
    _inherit = ['todo.task']
    
    stage_id = fields.Many2one(
        string=u'Stage',
        comodel_name='todo.task.stage',
        ondelete='set null',
    )
    tag_ids = fields.Many2many(
        string=u'Tags',
        comodel_name='todo.task.tag',
    )

    
    refers_to = fields.Reference(
        string=u'Refers to',
        selection=[('res.users', 'User'),('res.partner', 'Partner')]
    )
    stage_state = fields.Selection(
        string=u'Stage State',
        related='stage_id.state'
    )
    
    def compute_user_todo_count(self):
        self.user_todo_count=self.search_count([('user_id','=',self.user_id.id)])
    
    user_todo_count = fields.Integer(
        string=u'User To-Do Count',compute='compute_user_todo_count'
    )
    
    
    

    



class Stage(models.Model):
    """ todo.task.stage

    Fields:
      name (Char): Human readable name which will identify each record.

    """

    _name = 'todo.task.stage'
    _description = u'To-do Stage'
    _order = 'sequence,name'
    
    name = fields.Char(
        string=u'Name',size=40
    )
    desc = fields.Text(
        string=u'Description',
    )
    state = fields.Selection(
        string=u'State',
        selection=[('draft', 'New'), ('open', 'Started'),('done','Closed')]
    )
    docs = fields.Html(
        string=u'Documentation',
    )
    sequence = fields.Integer(
        string=u'Sequence',
    )
    perc_complete = fields.Float(
        u'% Complete',(3,2)
    )
    date_effective = fields.Date(
        string=u'Effective Date',
        default=fields.Date.context_today,
    )
    date_changed = fields.Datetime(
        string=u'Last Changed',
        default=fields.Datetime.now,
    )
    fold = fields.Boolean(
        string=u'Folded?',
    )
    image = fields.Binary(
        string=u'Image',
    )
    

    
    class Tags(models.Model):
        """ 标记task的tag，一个task可以标记多个tags
    
        Fields:
          name (Char): Human readable name which will identify each record.
    
        """
    
        _name = 'todo.task.tag'
        _description = u'To-do Tag'
        
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
        parent_left = fields.Integer(
            string=u'Parent Left',
            index=True, 
        )
        
        parent_right = fields.Integer(
            string=u'Parent Right',
            index=True,
        )
       
        
        
        
    
    
        
    
    
    
    
    
    
    
    
    
    




    

