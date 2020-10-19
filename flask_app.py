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
    #spécifier la relation entre les deux classes
    email= db.relationship('Email', backref='sender', lazy=True)

    #comment l'objet sera printé 
    def __repr__(self):
        return f"User('{self.nom}','{self.prenom}','{self.login}')"#on ne montre pas le mot de passe quand on voudra le représenter

class Email(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    texte = db.Column(db.Text, nullable=False) 
    categorie_model = db.Column(db.String(100), nullable=False)
    categorie_choisie= db.Column(db.String(100), nullable=False)
    #Foreign key 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

     #comment l'objet sera printé 
    def __repr__(self):
        return f"Email('{self.categorie_model}','{self.categorie_choisie}')"

    

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/administrateur')
def admin():
    return render_template('administrateur.html')

#permet de runner l'application directement dans python
if __name__ == '__main__':
    app.run(debug=True)
