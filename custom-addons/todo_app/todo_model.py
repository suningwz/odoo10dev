
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class TodoTask(models.Model):
    _name= 'todo.task'
    _description= 'To-do Task description'
    name = fields.Char(
        string=u'Description',
        required=True,
    )
    
    is_done = fields.Boolean(
        string=u'Done?',
    )
    
    active = fields.Boolean(
        string=u'Active',default=True,
    )
    
    
    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done=not task.is_done
        return True

    @api.model
    def do_clear_done(self):
        dones=self.search([('is_done','=',True)])
        dones.write({'active':False})
        return True