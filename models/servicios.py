from odoo import models, fields, api
from datetime import date

class TallerServicios(models.Model):
	# nombre del modelo y su descripcion. asi lo reconoce odoo
	_name = 'taller.servicios'  
	_description = 'descripcion sin gluten del servicio'  # descripcion del modelo

	# ahora los campos, que son los que se van a usar en la base de datos

	# 'name' es el nombre del servicio, obligatorio
	name = fields.Char(required=True, string='numero de servicio')  
	# 'tipo' es el tipo de servicio, tiene tres opciones y el por defecto es el mantenimiento
	tipo = fields.Selection([('1', 'Mantenimiento anual'), ('2', 'Avería'), ('3', 'Mejora')], default='1', required=True)  
	# 'presupuesto' es un campo de texto para poner el presupuesto del servicio
	presupuesto = fields.Char(required=True)  
	# 'proxima' es la fecha en que se hace el siguiente servicio
	proxima = fields.Date(compute='_compute_proxima', store=True)  
	# 'piezas_ids' son las piezas relacionadas con el servicio, una relacion de uno a muchos con el modelo 'taller.piezas'
	piezas_ids = fields.One2many('taller.piezas', 'servicio_id')  
	# 'coche_id' es para asociar un coche al servicio
	coche_id = fields.Many2one('taller.coches')  
	# 'oculto' es un booleano que depende del tipo de servicio, para ver si lo mostramos o no
	oculto = fields.Boolean(compute='_compute_oculto')  

	@api.depends('tipo')  
	def _compute_oculto(self):  
		for record in self:
			# si es mantenimiento anual, no lo ocultamos
			record.oculto = record.tipo != '1'  # True si no es '1', False si es '1'

	@api.depends('tipo')  
	def _compute_proxima(self):  
		for record in self:
			if record.tipo == '1':  # Si es mantenimiento anual
				record.proxima = date.today().replace(year=date.today().year + 1)
			else:
				record.proxima = False  # Fecha vacía en Odoo es False
