
{
    'name': "To-Do Kanban",

    'summary': """Kanban, Todo, Tasks""",
    'description': """Kanban board for To-Do Tasks.""",

    'author': "Abdul Halim",
    'website': "http://aristobd.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    'depends': ['todo_ui'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/todo_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
