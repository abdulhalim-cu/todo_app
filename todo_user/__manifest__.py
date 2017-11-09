# -*- coding: utf-8 -*-
{
    'name': "todo_user",

    'summary': """To-Do User Extension""",

    'description': """Extended To-Do Task """,

    'author': "Abdul Halim",
    'website': "http://aristobd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['todo_app', 'mail'],
    'application':True,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/todo_view.xml',
        'views/todo_task.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
