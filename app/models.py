from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from app import db

class Incident(db.Model):
    __tablename__ = 'incidents'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.String(1255))
    customer_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    tags = db.Column(db.Text())
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    customers = relationship('Customer',secondary='transactions')
    category = db.relationship('Category', backref=db.backref('inc', lazy='dynamic'))

    def __init__(self,title,descritpion,customer_id,category_id,start_date):
        self.title = title
        self.description = description
        self.customer_id = customer_id
        self.category_id = category_id
        self.start_date = start_date

    def __repr__(self):
        return f'Incident -> {self.title}'

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(80))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(18))
    mobile = db.Column(db.String(18))
    workphone = db.Column(db.String(18))
    fax = db.Column(db.String(18))
    email = db.Column(db.String(120))
    details = db.Column(db.Text)
    incidents = relationship('Incident',secondary='transactions')

    def __init__(self,firstname,lastname,phone,mobile,workphone,fax,email,details):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.details = details

    def __repr__(self):
        return f'Customer -> {self.mobile}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(120))

    def __init__(self, cat_name):
        self.cat_name = cat_name

    def __repr__(self):
        return f'Category -> {self.cat_name}'

    def CategoryList():
        return Category.query.all()

class Transactio(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer,primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    incident_id = db.Column(db.Integer, db.ForeignKey('incidents.id'))
    t_incident = relationship('Incident',backref=backref('transactions'))
    t_customer = relationship('Customer',backref=backref('transactions'))
