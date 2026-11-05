from odoo import models, fields, api


class GpResponsables(models.Model):
    _name = 'gp.responsables'
    _description = 'Responsables de Propiedades'

    name = fields.Char(string='Nombre del Responsable', required=True)
    email = fields.Char(string='Correo Electrónico')
    telefono = fields.Char(string='Teléfono')
    tipo = fields.Selection([
        ('llaves', 'Llaves'),
        ('limpieza', 'Limpieza'),
        ('arreglos', 'Arreglos'),
        ('otro', 'Otro'),
    ], string='Tipo de Responsable', required=True)
    
    usuario_id = fields.Many2one(
        'res.users',
        string='Usuario Asignado',
        ondelete='set null',
    )