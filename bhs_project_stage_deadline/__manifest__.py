{
    'name': 'Project Stage Deadline Control',
    'version': '19.0.0',
    'summary': 'Control task deadline visibility by project stage',
    'description': 'Show or hide deadlines on task Kanban cards according to the current project stage.',
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
