from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField, TextAreaField
from wtforms import EmailField, DateTimeField, SelectField
from wtforms import validators
from flask_wtf.csrf import CSRFProtect
import forms
from flask import Flask
from flask_wtf import FlaskForm
from models import Curso, Inscripcion


#app=Flask(__name__)
#app.secret_key='clave secreta'

#csrf=CSRFProtect()

class UserForm(FlaskForm):
    id=IntegerField('id')
    nombre=StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese un nombre valido")
        ])
    apellidos=StringField("apellidos", [
        validators.DataRequired(message="El campo es requerido")])
    correo=EmailField("correo", [
        validators.DataRequired(message="El campo es requerido")])
    telefono=StringField("telefono", [
        validators.DataRequired(message="El campo es requerido")])

 
class UserForm2(FlaskForm):
    matricula=IntegerField('matricula')
    nombre=StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese un nombre valido")
        ])
    apellidos=StringField("apellidos", [
        validators.DataRequired(message="El campo es requerido")])
    especialidad=StringField("especialidad", [
        validators.DataRequired(message="El campo es requerido")])
    email=StringField("email", [
        validators.DataRequired(message="El campo es requerido")])


class UserForm3(FlaskForm):
    id=IntegerField('id')
    nombre=StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=100, message="Ingrese un nombre valido")
        ])
    descripcion=TextAreaField("descripcion", [
        validators.DataRequired(message="El campo es requerido")])
    maestro_id=SelectField(
        "Maestro",
        coerce=int,
        validators= [validators.DataRequired(message="El campo es requerido")
        ])
    def validate_nombre(self, field):
        curso = Curso.query.filter(Curso.nombre == field.data).first()
        if curso:
            raise validators.ValidationError("Ese curso ya existe y ya tiene un maestro asignado")


class UserForm4(FlaskForm):
    id=IntegerField('id')
    alumno_id = SelectField("Alumno", coerce=int, validators=[
        validators.DataRequired(message="El campo es requerido")
    ])

    curso_id = SelectField("Curso", coerce=int, validators=[
        validators.DataRequired(message="El campo es requerido")
    ])
    fecha=DateTimeField("fecha", [
        validators.DataRequired(message="El campo es requerido")
        ])
    def validate_alumno_id(self, field):
        inscripcion=Inscripcion.query.filter(Inscripcion.alumno_id== field.data,
                                             Inscripcion.curso_id== self.curso_id.data).first()
        if inscripcion:
            raise validators.ValidationError("Este alumno ya esta inscrito en este curso")