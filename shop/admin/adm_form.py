from wtforms import BooleanField, StringField, PasswordField, validators, ValidationError
from flask_wtf import FlaskForm, Form
from .adm_db_form import User


class RegistrationForm(FlaskForm):
    name = StringField('Имя', [validators.Length(min=4, max=25)])
    username = StringField('Имя пользователя', [validators.Length(min=4, max=25)])
    email = StringField('Почта', [validators.Length(min=6, max=35)])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Пароль должен совпадать')
    ])
    confirm = PasswordField('Повторите пароль')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Такое имя пользователя уже занято, придумайте другое')

        
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Почта уже зарегистрирована')
            


class LoginForm(FlaskForm):
    email = StringField('Почта', [validators.Length(min=6, max=35)])
    password = PasswordField('Пароль', [validators.DataRequired()])