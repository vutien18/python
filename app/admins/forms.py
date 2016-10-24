
# from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField,validators,PasswordField
from app.admins.models import User
class SigupForm(FlaskForm):
    username=TextField('username',[validators.Required('Please enter your username'),validators.Length(max=30,message='Username is at most 30 characters.')])
    email=TextField('email',[validators.Required('Please enter your email address.'),validators.Email('Please enter email add ress')])
    password=PasswordField('password',[validators.Required('Please enter a password'),validators.Length(min=6,message='Passwords is at least 6 characres.'),validators.EqualTo('confirm',message='Passwords must match')])
    role=TextField('role')
    confirm=PasswordField('Repeat Password')
    submit=SubmitField('Create account')

class LoginForm(FlaskForm):
    username=TextField('username',[validators.Required('Enter username')])
    password=PasswordField('password',[validators.Required('Enter password '),validators.length(min=6,message='password is at 6 character')])

def __init__(self,*args,**kwargs):
    FlaskForm.__init__(self,*args,**kwargs)

def __init__(self,*args,**kwargs):
    FlaskForm.__init__(self,*args,**kwargs)

def validate(self):
    print('in validate')
    if not FlaskForm.validate(self):
        return False
    user=User.query.filter_by(username=self.username.data).first()
    if user:
        self.username.errors.append('That username is already taken.')
    user_email = User.query.filter_by(email=self.email.data).first()
    if user_email:
        self.username.errors.append('That email is already taken.')
        return False

    return True
