from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class Add(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired(), Length(min=10, max=35)])
    text = StringField('Напишите что-нибудь...', validators=[DataRequired(), Length(min=60, max=255)])
    submit = SubmitField('Создать')


class Login(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')