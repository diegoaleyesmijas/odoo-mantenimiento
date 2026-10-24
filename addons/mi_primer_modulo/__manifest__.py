{
    'name': 'Mi Primer Módulo',
    'version': '18.0.1.0.0',
    'summary': 'Este es mi primer módulo en Odoo',
    'category': 'Practicas',
    'author': 'Diego Leyes',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/demo_views.xml',
        'views/tecnico_views.xml',
        ],
    'installable': True,
    'application': False,
}
