
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(100))
    email = db.Column(db.String(45))
    role = db.Column(db.SmallInteger)

    def __init__(self, username, email, password,role):
        self.username = username
        self.email = email.lower()
        self.set_password(password)
        self.role=role
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '' % (self.username)