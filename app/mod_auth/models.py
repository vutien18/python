# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
# from werkzeug.security import generate_password_hash,check_password_hash
from app import db
# class User(db.Model):
#     __tablename__ = 'users'
#     uid = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(120), unique=True)
#     password = db.Column(db.String(54))
#
#     def __init__(self, name, email, password):
#         self.firstname = name.title()
#         self.email = email.lower()
#         self.set_password(password)
#
#     def set_password(self, password):
#         self.pwdhash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.pwdhash, password)


# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'admin'

    # User Name
    name    = db.Column(db.String(128),  nullable=False)

    # Identification Data: email & password
    email    = db.Column(db.String(128),  nullable=False,
                                            unique=True)
    password = db.Column(db.String(192),  nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

# from flask.ext.sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# # db = SQLAlchemy()
# class User(db.Model):
#     __tablename__ = 'users'
#     uid = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(100))
#     lastname = db.Column(db.String(100))
#     email = db.Column(db.String(120), unique=True)
#     pwdhash = db.Column(db.String(54))
#
#     def __init__(self, firstname, lastname, email, password):
#         self.firstname = firstname.title()
#         self.lastname = lastname.title()
#         self.email = email.lower()
#         self.set_password(password)
#
#     def set_password(self, password):
#         self.pwdhash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.pwdhash, password)