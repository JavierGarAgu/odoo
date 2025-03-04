from odoo import models, fields, api
from datetime import date

class TallerCoches(models.Model):
    # Este es el modelo que maneja los coches en el taller
    _name = 'taller.coches'  # nombre del modelo
    _description = 'Modelo para gestionar vehículos en el taller'  # descripción

    # 'name' es el número de chasis, es obligatorio
    name = fields.Char(required=True, string='Número de chasis')  
    # 'matricula' es la matrícula del coche, también obligatorio
    matricula = fields.Char(required=True)  
    # 'modelo' es el modelo del coche, y también obligatorio
    modelo = fields.Char(required=True)  
    # 'mantenimiento_requerido' indica si el coche necesita mantenimiento
    # Lo calculamos con una función y lo guardamos para no tener que recalcularlo todo el rato
    mantenimiento_requerido = fields.Boolean(compute='_compute_mantenimiento_requerido', store=True)  
    # Relacionamos los servicios que se le han hecho a este coche
    servicios_ids = fields.One2many('taller.servicios', 'coche_id')  
    # Relacionamos el cliente que tiene este coche
    cliente_id = fields.Many2one('taller.clientes')  

    # Esta función se encarga de calcular si el coche necesita mantenimiento o no
    @api.depends('servicios_ids.proxima', 'servicios_ids.tipo')
    def _compute_mantenimiento_requerido(self):
        hoy = date.today()  # Hoy para comparar las fechas de los servicios
        for coche in self:
            # Inicializamos mantenimiento como False, por si acaso
            mantenimiento = False  
            # Miramos todos los servicios asociados al coche
            for servicio in coche.servicios_ids:
                # Si encontramos un servicio de tipo '1' (Mantenimiento anual) y la fecha próxima es hoy o antes
                if servicio.tipo == '1' and servicio.proxima <= hoy:
                    mantenimiento = True  # Si es así, el coche necesita mantenimiento
                    break  # Ya no necesitamos seguir buscando, salimos del bucle
            # Le asignamos el valor a la variable mantenimiento_requerido
            coche.mantenimiento_requerido = mantenimiento  
