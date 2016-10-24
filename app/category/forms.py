from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField,validators,SubmitField
class CategoryForm(FlaskForm):
    name=TextField('Name',[validators.Required('Please enter your name'),validators.Length(max=10,message='name is at most 30 characters.')])
    category_id=TextField('category_id')
    postion=TextField('position')