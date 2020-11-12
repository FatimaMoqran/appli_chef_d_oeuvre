from flask_app import db, login_manager
from flask_login import UserMixin

#permet de logger les differents user 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String, nullable=False)
    login_email = db.Column(db.String(20), unique= True, nullable= False)
    mot_de_passe = db.Column(db.String(60), nullable = False)
    #spécifier la relation entre les deux classes
    email_text = db.relationship('Email', backref='sender', lazy=True)

    #comment l'objet sera printé 
    def __repr__(self):
        return f"User('{self.pseudo}','{self.login_email}')"#on ne montre pas le mot de passe quand on voudra le représenter

class Email(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    texte = db.Column(db.Text, nullable=False) 
    categorie_model = db.Column(db.String(100), nullable=False)
    categorie_choisie= db.Column(db.String(100), nullable=False)
    #Foreign key 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

     #comment l'objet sera printé 
    def __repr__(self):
        return f"Email('{self.categorie_model}','{self.categorie_choisie}')"#on ne montre pas le texte car ça peut être trs long

class Categorie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    label = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Categorie('{self.id}',{self.label}')" #afficher les categories et leur libelle 