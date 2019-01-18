from app import app
from app import db
from app.models import Incident, Customer, Category

def MakeQuery(**kwargs):
    queryStr = (db.session.query(*Incident.__table__.columns, *Customer.__table__.columns, *Category.__table__.columns)
                .filter(Incident.customer_id == Customer.id).filter(Incident.category_id == Category.id))
    for j, k in kwargs.items():
        varValue = k.split('|')
        if varValue[0] != '':
            if varValue[2] == 'Incident':
                if varValue[1] == 'eq':
                    queryStr = queryStr.filter((getattr(Incident, j)) == varValue[0])
                if varValue[1] == 'like':
                    queryStr = queryStr.filter((getattr(Incident, j)).like('%'+varValue[0]+'%'))
            elif varValue[2] == 'Customer':
                if varValue[1] == 'eq':
                    queryStr = queryStr.filter((getattr(Customer, j)) == varValue[0])
                if varValue[1] == 'like':
                    queryStr = queryStr.filter((getattr(Customer, j)).like('%'+varValue[0]+'%'))
    return queryStr

def MakeQueryAll():
    queryStr = (db.session.query(*Incident.__table__.columns, *Customer.__table__.columns, *Category.__table__.columns)
                .filter(Incident.customer_id == Customer.id).filter(Incident.category_id == Category.id)).order_by(Incident.start_date.desc())
    return queryStr
