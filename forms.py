from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField
from wtforms import EmailField
from wtforms import validators
from flask_wtf.csrf import CSRFProtect
import forms
from flask import Flask
from flask_wtf import FlaskForm


#app=Flask(__name__)
#app.secret_key='clave secreta'

#csrf=CSRFProtect()

class UserForm(FlaskForm):
    id=IntegerField('id')
    nombre=StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese un nombre valido")
        ])
    apaterno=StringField("apaterno", [
        validators.DataRequired(message="El campo es requerido")])
    correo=EmailField("correo", [
        validators.DataRequired(message="El campo es requerido")])
   