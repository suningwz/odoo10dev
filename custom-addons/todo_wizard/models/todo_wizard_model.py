
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
    _name='todo.wizard'
    _description='To-do Mass Assignment'
    
    task_ids = fields.Many2many(
        string=u'Tasks',
        comodel_name='todo.task',
    )
    
    new_user_id = fields.Many2one(
        string=u'Responsible',
        comodel_name='res.users',
    )
    
    new_deadline = fields.Date(
        string=u'Deadline to Set',
        default=fields.Date.context_today,
    )

    @api.multi
    def do_mass_update(self):
        
        self.ensure_one()
        if not (self.new_deadline or self.new_user_id):
            raise exceptions.ValidationError('No data to update')
        if not len(self.task_ids):
            raise exceptions.ValidationError('No records to update')
        _logger.debug('Mass update on Todo Tasks %s',self.task_ids.ids)

        vals={}
        if self.new_deadline:
            vals['date_deadline']=self.new_deadline
        if self.new_user_id:
            vals['user_id']=self.new_user_id

        if vals:
            self.task_ids.write(vals)
        
        return True

    @api.multi
    def do_count_tasks(self):
        Task=self.env['todo.task']
        count=Task.search_count([('is_done','=',False)])
        raise exceptions.Warning('There are %d active tasks.' %count)

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        return {
            'type':'ir.actions.act_window',
            'res_model':self._name,
            'res_id':self.id,
            'view_mode':'form',
            'view_type':'form',          
            'target':'new'
    }

    @api.multi
    def do_populate_tasks(self):
        
        self.ensure_one()
        Task=self.env['todo.task']
        all_tasks=Task.search([('is_done','=',False)])
        self.task_ids=all_tasks
        return self._reopen_form()


#    
    