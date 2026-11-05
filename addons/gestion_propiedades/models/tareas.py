from odoo import models, fields, api

class GpTareas(models.Model):
    _name = 'gp.tareas'
    _description = 'Tareas de Propiedades'

    name = fields.Char(string='Nombre de la Tarea', required=True)
    descripcion = fields.Text(string='Descripción de la Tarea')
    tipo_tarea = fields.Selection([
        ('llaves', 'Llaves'),
        ('limpieza', 'Limpieza'),
        ('arreglo', 'Arreglo'),
        ('otro', 'Otro'),
    ], string='Tipo de Tarea',)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_curso', 'En Curso'),
        ('completada', 'Completada'),
    ], string='Estado de la Tarea', required=True, default='pendiente')
    prioridad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ], string='Prioridad', required=True, default='media')
    fecha_programada = fields.Date(string='Fecha Programada')
    fecha_limite = fields.Date(string='Fecha Límite')
    horas = fields.Float(string='Horas Invertidas', default=0.0)
    propiedad_id = fields.Many2one(
        
        'gp.propiedades',
        ondelete='restrict',
        string='Propiedad',
    )
    responsable_id = fields.Many2one(
        'gp.responsables',
        string='Responsable de la Tarea',
        ondelete='set null',
    )
