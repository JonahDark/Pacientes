from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class visita_model(models.Model):
    _name = 'pacientes_app.visita_model'
    _description = 'Modelo de visita'

    visita = fields.Many2one("pacientes_app.paciente_model",index=True,string="Paciente",help="Paciente de la visita")
    fecha = fields.Date(string="Fecha",default=datetime.today())
    detalle = fields.Html(string="Detalle",required=True,help="Detalle de la cita")
    
