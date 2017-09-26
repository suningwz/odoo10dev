
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo import exceptions
import logging
_logger=logging.getLogger(__name__)


class TodoWizard(models.TransientModel):
    """
    The summary line for a class docstring should fit on one line.
    """
    _name = 'todo.wizard'
    _description = u'todo.wizard for updating fields of todo.task model'
    
    
    new_date_deadline = fields.Date(
        string=u'Deadline to Set',
        default=fields.Date.context_today,
    )
    new_user_id = fields.Many2one(
        string=u'Responsible',
        comodel_name='res.users',
        ondelete='set null',
    )
    
    task_ids = fields.Many2many(
        string=u'Tasks',
        comodel_name='todo.task',
    )
    
    
    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        
        return {
            'name': _('Reopen Wizard Form for todo.task'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': self._name,
            'res_id': self.id,
            'target':'new'
        }

    @api.multi
    def do_populate_tasks(self):
        self.ensure_one()
        task=self.env['todo.task']
        open_tasks=task.search([('is_done','=',False)])
        self.task_ids=open_tasks
        return self._reopen_form()

    @api.multi
    def do_count_tasks(self):
        task=self.env['todo.task']
        count=task.search_count([('is_done','=',False)])
        raise exceptions.Warning('There are %d active tasks.' %count)

    @api.multi
    def do_mass_update(self):
        self.ensure_one()
        if not (self.new_date_deadline or self.new_user_id):
            raise exceptions.ValidationError('No data to update')
        _logger.warning('Mass update on todo.task %s',self.task_ids.ids)
        vals={}
        if self.new_user_id:
            vals['user_id']=self.new_user_id
        if self.new_date_deadline:
            vals['date_deadline']=self.new_date_deadline
        self.task_ids.write(vals)
        return True
        
        
        
    
    
    
 
    
    
    
    
    
    

