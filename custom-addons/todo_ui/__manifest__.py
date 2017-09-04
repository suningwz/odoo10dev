
# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Copyright (c) All rights reserved:
#        (c) 2015  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
###############################################################################
{
    'name': 'User interface improvements to the To-Do app',
    'summary': 'User interface improvements to the To-Do app  Module Project',
    'version': '1.0',

    'description': """
User interface improvements to the To-Do app  Module Project.
==============================================


    """,

    'author': 'xiaoye',
    'maintainer': 'xiaoye',
    'contributors': ['xiaoye <xiaoye@gmail.com>'],

    'website': 'http://www.gitlab.com/xiaoye',

    'license': 'AGPL-3',
    'category': 'Uncategorized',

    'depends': [
        'todo_user'
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': ['views/todo_menu.xml',
    'views/todo_view.xml'
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
