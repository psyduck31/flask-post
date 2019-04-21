from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class Add(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    text = StringField('Напишите что-нибудь...', validators=[DataRequired()])
    submit = SubmitField('Создать')


class Login(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class Registration(FlaskForm):
    username = StringField('Введите имя аккаунта', validators=[DataRequired()])
    password = PasswordField('Введите пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')