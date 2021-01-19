from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class paciente_model(models.Model):
    _name = 'pacientes_app.paciente_model'
    _description = 'Modelo de paciente'
    _sql_constraints = [("dni_unico", "UNIQUE(dni)", "Este DNI ya existe"), ]

    foto = fields.Binary()
    dni = fields.Char(string="DNI", required=True,
                      index=True, help="DNI del paciente")
    name = fields.Char(string="Nombre", required=True,
                       help="Nombre del paciente")
    apellidos = fields.Char(
        string="Apellidos", required=True, help="Apellidos del paciente")
    fechaNac = fields.Date()
    telefono = fields.Char(string="Telefono", required=True,
                           help="Telefono del paciente")
    email = fields.Char(string="Email", required=True,
                        help="Email del paciente")
    visitas = fields.One2many(
        "pacientes_app.visita_model", "visita", string="Historial de Visitas")

    numVisitas = fields.Integer(
        string="Visitas", compute="_numVisitas", help="Numero de visitas")

    @api.depends("visitas")
    def _numVisitas(self):
        self.numVisitas = len(self.visitas)

    @api.constrains("dni")
    def _validacionDNI(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = self.dni[:-1]
        posi = int(num) % 23
        if letra != letras[posi]:
            raise ValidationError("DNI no valido")
        if len(self.dni) > 9:
            raise ValidationError("El DNI no puede ser mayor de 9 caracteres")
        if letra.isnumeric():
            raise ValidationError("El DNI debe terminar con una letra")

    @api.constrains("email")
    def _validacionEmail(self):
        if "@" not in self.email:
            raise ValidationError("El email debe contener un @")
        if ".com" not in self.email and ".es" not in self.email:
            raise ValidationError("El email debe contener un .com o .es")

    @api.constrains("fechaNac")
    def _esMayorDeEdad(self):
        añoHoy = datetime.today().year
        añoNac = self.fechaNac.year
        if (añoHoy - añoNac) < 18:
            raise ValidationError("El paciente debe de ser mayor de edad")
