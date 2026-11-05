{
    'name': 'Gestion de Propiedades',
    'summary': 'CRUD de propiedades y tareas de mantenimiento para inmobiliaria',
    'description': """
        App para gestionar propiedades de alquiler turístico y tareas de mantenimiento asociadas. Permite crear, leer, actualizar y eliminar propiedades, así como registrar y asignar tareas de mantenimiento a cada propiedad. Incluye funcionalidades de notificaciones y seguimiento de tareas.
    """,
    'author': 'Diego Leyes',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['base','mail'],
    'data': [   
        'views/propiedades_views.xml',
    ],  
    'category': 'Website/Management',   
 
    'assets': {},
    'application': True,
    'installable': True,
}
