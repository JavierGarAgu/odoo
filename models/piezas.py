from odoo import models, fields

class TallerPiezas(models.Model):
	# nombre del modelo y su descripcion, pa que odoo lo entienda
	_name = 'taller.piezas'  
	_description = 'descripcion sin gluten de las piezas'  # descripción de las piezas

	# campos del modelo, los que usaremos en la base de datos

	# 'name' es el nombre de la pieza, obligatorio
	name = fields.Char(required=True, string='nombre')  
	# 'tipo' es el tipo de pieza, tiene 3 opciones: transmision, perifericos o motor
	tipo = fields.Selection([('1', 'Transmisión'), ('2', 'Periféricos'), ('3', 'Motor')], default='2', required=True)  
	# 'servicio_id' relaciona la pieza con un servicio (modelo 'taller.servicios')
	servicio_id = fields.Many2one('taller.servicios')  
