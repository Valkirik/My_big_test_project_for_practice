from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField("User name", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    config_password = PasswordField('Enter a password again', validators=[DataRequired(), EqualTo('password')])
    submit = StringField("enter")

    def validate_usernamen(self, username):
        user = User.quiry.filter_by(usernam=username.data)