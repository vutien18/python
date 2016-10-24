# Import Form and RecaptchaField (optional)
from flask.ext.wtf import Form # , RecaptchaField
from flask_wtf import Form
# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField,validators,SubmitField # BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo

class LoginForm(Form):
    email    = TextField('Email Address', [Email(),
                Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
                Required(message='Must provide a password. ;-)')])
class SignForm(Form):
    name = TextField('name', [
        validators.Required('Please enter your username.'),
        validators.Length(max=30, message='Username is at most 30 characters.'),
    ])
    email = TextField('Email', [
        validators.Required('Please enter your email address.'),
        validators.Email('Please enter your email address.')
    ])
    password=PasswordField('Password',[Required(message='Required pass')])
    submit = SubmitField('Create account')