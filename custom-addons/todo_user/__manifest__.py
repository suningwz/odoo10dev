
# -*- coding: utf-8 -*-
###############################################################################

#    Copyright (c) All rights reserved:

###############################################################################
{
    'name': 'Mulitiuser To-Do',
    'summary': 'Mulitiuser To-Do Module Project',
    'version': '1.0',

    'description': """
Mulitiuser To-Do Module Project.
==============================================


    """,

    'author': 'xiaoye',
    'maintainer': 'xiaoye',
    'contributors': ['xiaoye <xiaoye@gmail.com>'],

    'website': 'http://www.gitlab.com/xiaoye',

    'license': 'AGPL-3',
    'category': 'Uncategorized',

    'depends': [
        'todo_app','mail'
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': ['views/todo_task.xml',
    'views/todo_menu.xml',
    'security/todo_access_rules.xml'
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
