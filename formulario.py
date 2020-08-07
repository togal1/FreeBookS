from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#StringField funcion validadora , DataRequired, length valida datos que no pueden estar vacíos y longitud de 2 a 20 caracteres
class RegistroForm(FlaskForm):
    User_nick=StringField('usuario_nick', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": " Nick"})
    User_email = StringField('usuario_email', validators=[DataRequired(), Email()], render_kw={"placeholder": " Email"})
    User_pass = PasswordField('usuario_pass', validators=[DataRequired()], render_kw={"placeholder": " Contraseña"})
    User_confiPass = PasswordField('usuario_confiPass', validators=[DataRequired(), EqualTo('usuario_pass')], render_kw={"placeholder": " Repita la contraseña"})
    Registrar=SubmitField('Regístrese aquí')

