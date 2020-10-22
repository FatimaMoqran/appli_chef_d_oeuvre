from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#instancie l'application
app = Flask(__name__)

#configurer la base de donnée (pour l'instant une SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#SQLAlchemy instance 
db = SQLAlchemy(app)

from flask_app import routes 