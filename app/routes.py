from flask import Flask, render_template, url_for, redirect, request, flash
from app import app
from app import db
from app.models import Incident, Customer, Category
from app.forms import CustomerForm, TicketForm, SeekCustomerForm, SeekTicketForm
from app.myfuncs import MakeQuery, MakeQueryAll

@app.route('/')
@app.route('/home')
def home():
    allIncidents = Incident.query.all()
    return render_template('dashboard.html', allIncidents=allIncidents)

@app.route('/editticket/<id>')
def EditTicket(id):
    return render_template('modifyticket.html', id=id)

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    noResult = ''
    seekQuery = Customer.query.all()
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
            noResult='Δεν Βρέθηκαν Αποτελέσματα'
        return render_template('customer.html', seekCustForm=seekCustForm, seekQuery=seekQuery, noResult=noResult)
    return render_template('customer.html', seekCustForm=seekCustForm, seekQuery=seekQuery)

@app.route('/addcustomer', methods=['GET', 'POST'])
def addcustomer():
    seekCustForm = SeekCustomerForm()
    custForm = CustomerForm()
    if custForm.validate_on_submit():
        newCustRec = Customer(custForm.firstName.data, custForm.lastName.data, custForm.address.data, custForm.phone.data, custForm.mobilePhone.data,
                    custForm.workPhone.data, custForm.faxPhone.data, custForm.email.data, custForm.details.data)
        db.session.add(newCustRec)
        db.session.commit()
        flash('Τα Στοιχεία Του Πελάτη Αποθηκεύτηκαν Με Επιτυχία')
        return render_template('customer.html', seekCustForm=seekCustForm)
    return render_template('customerfrm.html', custForm=custForm)

@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
    seekTicketForm = SeekTicketForm()
    seekQueryAll = MakeQueryAll()
    noResult = ''
    if seekTicketForm.validate_on_submit():
        seekTitle = seekTicketForm.ticketTitle.data
        seekServiceTag = seekTicketForm.serviceTag.data
        seekMobile = seekTicketForm.mobilePhone.data
        seekName = seekTicketForm.lastName.data
        if ( seekTicketForm.ticketCat.data == 1 ):
            seekTicketCat = ''
        else:
            seekTicketCat = seekTicketForm.ticketCat.data
        if seekTitle == '' and seekServiceTag == '' and seekMobile == '' and seekName == '' and seekTicketCat == '':
            seekQuery = MakeQuery()
        else:
            seekQuery = MakeQuery(title=seekTitle+'|like|Incident', serviceTag=seekServiceTag+'|like|Incident', category_id=str(seekTicketCat)+'|eq|Incident',
                        mobile=seekMobile+'|like|Customer', lastname=seekName+'|like|Customer')
        if seekQuery.count() == 0:
            noResult = 'Δεν Βρέθηκαν Αποτελέσματα'
        return render_template('ticket.html', seekTicketForm=seekTicketForm, seekQuery=seekQuery, noResult=noResult)
    return render_template('ticket.html', seekTicketForm=seekTicketForm, noResult=noResult, seekQuery=seekQueryAll)

@app.route('/addticket', methods=['GET', 'POST'])
def addticket():
    ticketForm = TicketForm()
    seekCustForm = SeekCustomerForm()
    return render_template('ticketfrm.html', ticketForm=ticketForm, seekCustForm=seekCustForm)
