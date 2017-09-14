
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.addons import decimal_precision as dp


class BaseArchive(models.AbstractModel):
    _name='base.archive'
    active = fields.Boolean(
        string=u'Active?',
        default=True
    )

    def do_archive(self):
        for record in self:
            record.active=not record.active

            

class LibraryBook(models.Model):
    """ The summary line for a class docstring should fit on one line.

    Fields:
      name (Char): Human readable name which will identify each record.

    """

    _name = 'library.book'
    
    _inherit = ['base.archive']
    
    _description = u'library book'

    _rec_name = 'short_name'
    _order = 'date_release desc,name'
    _sql_constraints = [('name_uniq','UNIQUE(name)','Book title must be unique.')]

    name = fields.Char(
        string=u'Title',
        required=True,
    )
    short_name = fields.Char(
        string=u'Short Title}',
    )
    notes = fields.Text(
        string=u'Internal Notes}',
    )
    state = fields.Selection(
        string=u'State',
        selection=[('draft', 'Not Available}'), ('available', 'Available'),('lost','Lost')]
    )
    description = fields.Html(
        string=u'Description',
    )
    cover = fields.Binary(
        string=u'Book Cover',
    )
    out_of_print = fields.Boolean(
        string=u'Out of Print?',
    )    
    date_release = fields.Date(
        string=u'Release Date',
        default=fields.Date.context_today,
    )
    last_updated = fields.Datetime(
        string=u'Last Updated',
        default=fields.Datetime.now,
    )
    pages = fields.Integer(
        string=u'Number of Pages',
    )
    reader_rating = fields.Float(
        string=u'Reader Average Rating',
        digits=(14, 4),
    )    
    
    cost_price = fields.Float(
        string=u'Book Cost',
        digits=dp.get_precision('BookPrice')
    )
    
    
    currency_id = fields.Many2one(
        string=u'Currency',
        comodel_name='res.currency',
    )
    retail_price=fields.Monetary(
        string=u'Retail Price',
        currency_field='currency_id'
        )
    

    author_ids = fields.Many2many(
        string=u'Authors}',
        comodel_name='res.partner',
    )
    publisher_id = fields.Many2one(
        string=u'Publisher',
        comodel_name='res.partner',
        ondelete='set null',
    )

    
    @api.constrains('date_release')
    def _check_date_release(self):
        for record in self:
            if record.date_release>fields.Date.today():
                raise models.ValidationError('Release date must be in the past.')

    
    age_days = fields.Float(
        string=u'Days since release',       
        compute='_compute_age',
        inverse='_inverse_age',
        search='_search_age'
    )

    @api.depends('date_release')
    def _compute_age(self):
        today=fields.Date.from_string(fields.Date.today())
        for record in self.filtered('date_release'):
            delta = fields.Date.from_string(record.date_release)-today
            self.age_days=delta.days    
    

    def _inverse_age(self):
        today=fields.Date.from_string(fields.Date.today())
        for book in self:
            book_release=today-datetime.timedelta(days=book.age_days)
            book.date_release=fields.Date.to_string(book_release)

    def _search_age(self,operator,value):
        today=fields.Date.from_string(fields.Date.today())
        value_days=datetime.timedelta(days=value)
        release_date=today-value_days
        value_date=fields.Date.to_string(release_date)
        return [('date_release',operator,value_date)]

   
    publisher_city = fields.Char(
        string=u'Publisher City',
        related='publisher_id.city',
    )
    state = fields.Selection(
        string=u'State',
        selection=[('draft', 'Unvailable'), ('available', 'Available'),('borrowed','Borrowed'),('lost','Lost')]
    )
  
    @api.model
    def is_allowed_transition(self,old_state,new_state):
        allowed = [('draft','unvailable'),('unvailable','vailable'),('vailable','borrowed'),('borrowed','available'),
        ('available','lost'),('borrowed','lost'),('lost','available')]
        return (old_state,new_state) in allowed

    @api.multi
    def change_state(self,new_state):
        for book in self:
            if book.is_allowed_transition(book.state,new_state):
                book.state=new_state
            else:
                continue
    


    
    
    



class ResPartner(models.Model):
    
    _inherit = ['res.partner']
    
    book_ids = fields.One2many(
        string=u'Published Books',
        comodel_name='library.book',
        inverse_name='pulisher_id',
    )  
    book_ids = fields.Many2many(
        string=u'Authored Books',
        comodel_name='library.book',
    )




class BookCategory(models.Model):
    _name='library.book.category'
    
    _parent_store = True
    
    name = fields.Char(
        string=u'Category',
    )
    parent_id = fields.Many2one(
        string=u'Parent Category',
        comodel_name='library.book.category',
        ondelete='restrict',
    )
    child_ids = fields.One2many(
        string=u'Child Categories',
        comodel_name='library.book.category',
        inverse_name='parent_id',
    )
    
    parent_left = fields.Integer('Left Parent', index=1)
    parent_right = fields.Integer('Right Parent', index=1)
    
    
    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive categories.')
            
    

class LibraryMember(models.Model):
    _name='library.member'
    _inherits = {'res.partner': 'partner_id'}
    
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        ondelete='cascade',
    )
    date_start = fields.Date(
        string=u'Member Since',
        default=fields.Date.context_today,
    )
    date_end = fields.Date(
        string=u'Termination Date',
        default=fields.Date.context_today,
    )
    member_number = fields.Char()
    
    
    
    
    
    

