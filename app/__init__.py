

from flask_migrate import Migrate
# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy

# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy  import  SQLAlchemy
# Define the WSGI application object
app = Flask(__name__)
app.config.from_object('config')
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
# from app.mod_auth.controllers import mod_auth as auth_module
# app.register_blueprint(auth_module)
from  app.admins.contronllers import model_admin as admins_module
app.register_blueprint(admins_module)
from app.category.controllers import model_category as category_module
app.register_blueprint(category_module)
db.create_all()