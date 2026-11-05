from odoo import models, fields, api

class GpHistorial(models.Model):
    _name = 'gp.historial'
    _description = 'Historial de Actividades'
    _order = 'fecha desc'

    tarea_id = fields.Many2one('gp.tareas', string='Tarea', ondelete='cascade')
    fecha = fields.Datetime(string='Fecha')
    descripcion = fields.Text(string='Descripción')
    horas = fields.Float(string='Horas', default=0.0)