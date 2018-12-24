from flask import Flask, render_template, url_for, redirect, request
from app import app
from app import db
from app.models import Incidents

@app.route('/')
@app.route('/home')
def home():
    allIncidents = Incidents.query.all()
    #listItems = ['1', '2', '3']
    return render_template('dashboard.html', mainTitle='KnowHow ServiceDesk', allIncidents=allIncidents) #, allIncidents=allIncidents)

@app.route('/editticket/<id>')
def EditTicket(id):
    return render_template('modifyticket.html', id=id)
