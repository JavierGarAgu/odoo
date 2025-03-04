# models/taller_vehiculos.py

from odoo import models, fields

class TallerClientes(models.Model):
    # este es el modelo para gestionar los clientes en el taller
    _name = 'taller.clientes'  # nombre del modelo
    _description = 'modelo para gestionar clientes en el taller'  # descripción

    # 'name' es el nombre del cliente, es obligatorio
    name = fields.Char(required=True, string='nombre')  
    # 'telefono' es el número de teléfono del cliente, opcional
    telefono = fields.Text()  
    # 'chasis_ids' es una relación de los coches asociados al cliente
    chasis_ids = fields.One2many('taller.coches', 'cliente_id')  

