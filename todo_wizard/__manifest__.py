# -*- coding: utf-8 -*-
{
    'name': "To-Do Tasks Management Assistant",

    'summary': """Mass edit your To-Do backlog.""", 
    'description': """
        Long description of module's purpose
    """,

    'author': "Abdul Halim",
    'website': "http://aristobd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['todo_user'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/todo_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
