from app import app
from app.models import Category
from flask_wtf import FlaskForm
from flask import Flask, render_template, flash, request
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms_sqlalchemy.fields import QuerySelectField

class CustomerForm(FlaskForm):
    firstName = StringField('Ονομα: ', validators=[DataRequired('First name Required')])
    lastName = StringField('Επίθετο: ', validators=[DataRequired('Last Name Id Required')])
    address = StringField('Διεύθυνση: ')
    phone = StringField('Τηλέφωνο: ')
    mobilePhone = StringField('Κινητό: ', validators=[DataRequired('Mobile Phone Is Required')])
    workPhone = StringField('Τηλέφωνο Εργασίας: ')
    faxPhone = StringField('FAX: ')
    email = StringField('Email: ', validators=[DataRequired('Email Required'), Email('Email Is Wrong')])
    details = TextAreaField('Επιπρόσθετα: ')
    submit = SubmitField('Αποθήκευση')

class SeekCustomerForm(FlaskForm):
    lastName = StringField('Επίθετο: ')
    mobilePhone = StringField('Κινητό: ')    

class TicketForm(FlaskForm):
    ticketTitle = StringField('Τίτλος', validators=[DataRequired('Title Field Must Not Be Null')])
    ticketDescr = TextAreaField('Περιγραφή')
    ticketCat = Category.CategoryList()
