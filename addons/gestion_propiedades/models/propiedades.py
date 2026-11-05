from odoo import models, fields, api 

class GpPropiedades(models.Model):
    _name = 'gp.propiedades'
    _description = 'Gestión de Propiedades'

    name = fields.Char(string='Nombre de la Propiedad', required=True)
    direccion = fields.Char(string='Dirección')
    tipo_propiedad = fields.Selection([
        ('piso', 'Piso'),
        ('casa', 'Casa'),
        ('local', 'Local'),
    ], string='Tipo de Propiedad', required=True)
    estado_alquiler = fields.Selection([
        ('disponible', 'Disponible'),
        ('alquilada', 'Alquilada'),
    ], string='Estado de Alquiler', required=True, default='disponible')
    responsable_id = fields.Many2one(
        'gp.responsables',
        string='Responsable',
        ondelete='set null', )
    notas = fields.Text(string='Notas')
   