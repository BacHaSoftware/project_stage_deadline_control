{
    'name': 'Project Stage Deadline Control',
    'version': '1.0',
    'summary': "Custom stage task",
    'description': 'Custom stage task',
    'author': 'Bac Ha Software',
    'website': 'https://bachasoftware.com/',
    'depends': ['project'],
    'data': [
        'views/project_task_views.xml',
        'views/task_stage_views.xml',
    ],
'assets': {
        'web.assets_frontend': [],
    },
    'external_dependencies': {
        'python': [],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}