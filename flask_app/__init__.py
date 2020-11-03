from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#instancie l'application
app = Flask(__name__)

#genere une secret key pour les formulaires afin de proteger les cookies 
#on genere la clé en python avec  la librairie secrets
app.config['SECRET KEY'] = '606c4261b169756bba33c5e36525d288'


#configurer la base de donnée (pour l'instant une SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#SQLAlchemy instance 
db = SQLAlchemy(app)

from flask_app import routes 