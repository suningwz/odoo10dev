
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, tools
from odoo.exceptions import UserError, ValidationError

class TodoReport(models.Model):
    _name = 'todo.task.report'
    _description = 'To-do Report'
    _auto = False

    name = fields.Char(
        string=u'Description',
    )
    is_done = fields.Boolean(
        string=u'Done?',
    )
    user_id = fields.Many2one(
        string=u'Responsible',
        comodel_name='res.users',
    )
    date_deadline = fields.Date(
        string=u'Deadline',
    )
    login = fields.Char(
        string=u'Email Address',
    )
    
    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr,'todo_task_report')
        self._cr.execute("""create view todo_task_report as 
    select tt.id,tt.name,is_done,user_id,date_deadline,ru.login  
    from todo_task as tt inner join res_users as ru on  tt.user_id=ru.id """)
    
    
    


