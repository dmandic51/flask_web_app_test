from wtforms import StringField
from wtforms import SubmitField
from wtforms import PasswordField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from flask_wtf import FlaskForm

from src.database import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):  ## FlaskForm specific behaviour
        user = User.query.filter_by(username=username_to_check.data)
        if user.first():
            raise ValidationError('Username already exists.')

    def validate_email_address(self, email_to_check):
        email =  User.query.filter_by(email_address=email_to_check.data)
        if email.first():
            raise ValidationError('Email already in use.')

    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email address:', validators=[Email(), DataRequired()])
    password_initial = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password_confirmation = PasswordField(label='Confirm password:',
                                          validators=[EqualTo('password_initial'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = StringField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
