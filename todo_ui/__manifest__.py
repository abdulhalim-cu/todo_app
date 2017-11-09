# -*- coding: utf-8 -*-
{
    'name': "User interface improvement to the To-Do app",

    'summary': """Todo, User UI Todo""",

    'description': """User friendly features """,

    'author': "Abdul Halim",
    'website': "http://aristobd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['todo_user'],

    'application': True,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/todo_view.xml',
        'views/todo_menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
