from flask.ext.sqlalchemy import SQLAlchemy
from app import db
class category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    position = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    def __init__(self, name, position, category_id):
        self.name = name
        self.position = position
        self.category_id = category_id
