from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#pour crypter les mots de passe
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


#instancie l'application
app = Flask(__name__)

#genere une secret key pour les formulaires afin de proteger les cookies 
#on genere la clé en python avec  la librairie secrets
#app.config['SECRET KEY'] = '606c4261b169756bba33c5e36525d288'


#configurer la base de données (pour l'instant une SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#SQLAlchemy instance 
db = SQLAlchemy(app)
#pour crypter les mots de passe
bcrypt = Bcrypt(app)
#pour pouvoir se connecter
login_manager = LoginManager(app)
#pour avoir acces à la login page
login_manager.login_view = 'login'
#avoir une alerte plus jolie avec bootstrap
login_manager.login_message_category = 'info'

from flask_app import routes 