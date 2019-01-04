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
    seekFlag = 0
    seekQuery = ''
    noResult = ''
    seekCustForm = SeekCustomerForm()
    if seekCustForm.validate_on_submit():
        print('Form Validated')
        seekName = seekCustForm.lastName.data
        seekMobile = seekCustForm.mobilePhone.data
        if seekName != '':
            seekFlag = 1
            print(f'Name Is -> {seekName}')
        if seekMobile != '':
            seekFlag += 2
            print(f'Mobile Is -> {seekMobile}')
        if seekFlag == 1:
            print(seekName+'%')
            seekQuery = Customer.query.filter(Customer.lastname.like('%'+seekName+'%')).all()
        if seekFlag == 2:
            seekQuery = Customer.query.filter(Customer.mobile.like('%'+seekMobile+'%')).all()
            print('Passed From Flag -> 2')
        if seekFlag == 0:
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
