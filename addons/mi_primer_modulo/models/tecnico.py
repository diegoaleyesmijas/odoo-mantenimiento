from odoo import models, fields

class Tecnico(models.Model):
        _name = 'mi_modulo.tecnico'
        _description = 'Tecnico de Mantenimiento'
    
        name = fields.Char(string='Nombre', required=True)
        email = fields.Char(string='Email')
        especialidad = fields.Selection([
            ('hardware', 'Hardware'),
            ('redes', 'Redes'),
            ('software', 'Software'),
        ], string='Especialidad', default='hardware')

