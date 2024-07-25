from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class MyForm(FlaskForm):

    email = StringField(label='Email', validators=[DataRequired(message='Invalid email address')])
    password = PasswordField(label='Password', validators=[DataRequired(message='Invalid password'), Length(min=8, message='Field must be atleast 8 characters long.')])
    login = SubmitField(label='Log In')
