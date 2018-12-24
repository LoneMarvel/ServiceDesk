from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

class Incidents(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.String(1255))
    customer = db.Column(db.String(120))
    category = db.Column(db.String(80))
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.now)


    def __repr__(self):
        return f"Items('{self.todo_title}')"
