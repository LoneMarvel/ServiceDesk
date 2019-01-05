from flask import Flask, render_template, url_for, redirect, request, flash
from app import app
from app import db
from app.models import Incident, Customer
from app.forms import CustomerForm, TicketForm, SeekCustomerForm

@app.route('/')
@app.route('/home')
def home():
    allIncidents = Incident.query.all()
    return render_template('dashboard.html', mainTitle='KnowHow ServiceDesk', allIncidents=allIncidents)

@app.route('/editticket/<id>')
def EditTicket(id):
    return render_template('modifyticket.html', id=id)

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    noResult = ''
    seekCustForm = SeekCustomerForm()
    if seekCustForm.validate_on_submit():
        seekName = seekCustForm.lastName.data
        seekMobile = seekCustForm.mobilePhone.data
        if seekName != '':
            seekQuery = Customer.query.filter(Customer.lastname.like('%'+seekName+'%')).all()
        if seekMobile != '':
            seekQuery = Customer.query.filter(Customer.mobile.like('%'+seekMobile+'%')).all()
        if  seekName == '' and seekMobile == '':
            seekQuery = Customer.query.all()
        if not seekQuery:
            noResult='No Results Found'
        return render_template('customer.html', seekCustForm=seekCustForm, seekQuery=seekQuery, noResult=noResult)
    return render_template('customer.html', seekCustForm=seekCustForm)

@app.route('/addcustomer')
def addcustomer():
    custForm = CustomerForm()
    return render_template('customerfrm.html', custForm=custForm)

@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
    ticketForm = TicketForm()
    return render_template('ticketfrm.html', ticketForm=ticketForm)
