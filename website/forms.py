from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class Add(FlaskForm):
    author = StringField('Автор', validators=[DataRequired(), Length(min=4, max=20)])
    title = StringField('Заголовок', validators=[DataRequired(), Length(min=10, max=35)])
    text = StringField('Напишите что-нибудь...', validators=[DataRequired(), Length(min=60, max=255)])
    submit = SubmitField('Создать')