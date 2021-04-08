
from wtforms import StringField
from wtforms import SubmitField
from wtforms import PasswordField
from flask_wtf import FlaskForm


class RegisterForm(FlaskForm):
    username = StringField(label='User name:')
    email_address = StringField(label='Email address:')
    password_initial = PasswordField(label='Password:')
    password_confirmation = PasswordField(label='Confirm password:')
    submit = SubmitField(label='Create Account')
