from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#instancie l'application
app = Flask(__name__)

#configurer la base de donnée (pour l'instant une SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#SQLAlchemy instance 
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String, nullable=False)
    login = db.Column(db.String(20), unique= True, nullable= False)
    mot_de_passe = db.Column(db.String(60), nullable = False)

    #comment l'objet sera printé 
    def __repr__(self):
        return f"User('{self.nom}','{self.prenom}','{self.login}')"

class Email(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/administrateur')
def admin():
    return render_template('administrateur.html')

#permet de runner l'application directement dans python
if __name__ == __name__:
    app.run(debug=True)
