from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

baseDir = os.path.abspath(os.path.dirname(__file__)) #'/home/tinos/Trainig/Python/ServiceDesk/app/'
app.config['SECRET_KEY'] = 'fa1f944ab8bd63090d9d4bc945bc0dfd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(baseDir, 'service.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes
