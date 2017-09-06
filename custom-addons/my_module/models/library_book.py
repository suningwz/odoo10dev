
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.addons import decimal_precision as dp

class LibraryBook(models.Model):
    """ The summary line for a class docstring should fit on one line.

    Fields:
      name (Char): Human readable name which will identify each record.

    """

    _name = 'library.book'
    _description = u'library book'

    _rec_name = 'short_name'
    _order = 'date_release desc,name'

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
        string=u'Retail Price'
        #currency_field='currency_id'
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
    child_id = fields.One2many(
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
            
    

   
        
    
    

