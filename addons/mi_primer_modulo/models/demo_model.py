from odoo import models, fields

class DemoModel(models.Model):
    _name = 'mi_modulo.demo'
    _description = 'Modelo de demostración'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha')
    activo = fields.Boolean(string='Activo', default=True)
   

    estado = fields.Selection([
        ('planificado', 'Planificado'),
        ('en_curso', 'En Curso'),
        ('completado', 'Completado'),
    ], string='Estado', default='planificado')

    prioridad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ], string='Prioridad', default='media')

    tecnico_id = fields.Many2one('mi_modulo.tecnico', string='Técnico')
    horas = fields.Float(string='Horas invertidas', default=0.0)
    fecha_limite = fields.Date(string='Fecha límite')
