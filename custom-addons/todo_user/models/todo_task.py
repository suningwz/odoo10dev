
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class TodoTask(models.Model):
    _name='todo.task'
    _inherit = ['todo.task','mail.thread']
    
    user_id = fields.Many2one(
        string=u'Responsible',
        comodel_name='res.users',
    )
    date_deadline = fields.Date(
        string=u'Deadline',
        default=fields.Date.context_today,
    )

    @api.multi
    def do_toggle_done(self):
        for task in self:
            if task.user_id != self.env.user:
                raise ValidationError('Only the responsible can do this!')
        return super(TodoTask,self).do_toggle_done()

    @api.multi
    def do_clear_done(self):
        domain=[('active','=',True),'|',('user_id','=',self.env.uid),('user_id','=',False)]
        done=self.search(domain)
        done.write({'active':False})
        return True
