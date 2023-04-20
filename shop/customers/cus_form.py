from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators, ValidationError
from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_wtf import FlaskForm
from .cus_db_form import Register


class CustomerRegisterForm(FlaskForm):
    name = StringField('Имя: ')
    username = StringField('Имя пользователя: ', [validators.DataRequired()])
    email = StringField('Почта: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Пароль: ', [validators.DataRequired(),
                                          validators.EqualTo('confirm', message=' Пароль должны совпадать!')])
    confirm = PasswordField('Повторите пароль: ', [validators.DataRequired()])
    country = StringField('Страна: ', [validators.DataRequired()])
    city = StringField('Город: ', [validators.DataRequired()])
    contact = StringField('Номер телефона: ', [validators.DataRequired()])
    address = StringField('Адрес: ', [validators.DataRequired()])
    zipcode = StringField('Почтовый индекс: ', [validators.DataRequired()])

    profile = FileField('Фото', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Только фотографии')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("Имя пользователя уже занято!")
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("Почта уже занята!")


class CustomerLoginFrom(FlaskForm):
    email = StringField('Почта: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Пароль: ', [validators.DataRequired()])

   




   

 

    

     

   


    

