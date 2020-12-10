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
    email = db.relationship('Email', backref='sender', lazy=True)

    #comment l'objet sera printé 
    def __repr__(self):
        return f"User('{self.pseudo}','{self.login_email}')"#on ne montre pas le mot de passe quand on voudra le représenter

class Email(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    texte = db.Column(db.Text, nullable=False)

    #foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    prediction_id= db.Column(db.Integer, db.ForeignKey('prediction.id'))
    choix_utilisateur_id = db.Column(db.Integer, db.ForeignKey('choix_utilisateur.id'))

    #spécifier la relation entre les deux classes
    prediction = db.relationship("Prediction", back_populates="email")
    choix_utilisateur = db.relationship("ChoixUtilisateur",back_populates="email")
     #comment l'objet sera printé 
    def __repr__(self):
        return f"Email('{self.texte}','{self.prediction_id}','{self.choix_utilisateur_id}')"#on ne montre pas le texte car ça peut être trs long
   

class Categorie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    label = db.Column(db.String(50), nullable=False)

    #spécifier la relation entre les deux classes
    prediction = db.relationship('Prediction')
    choix_utilisateur = db.relationship('ChoixUtilisateur')

    def __repr__(self):
        return f"Categorie('{self.id}','{self.label}')" #afficher les categories et leur libelle
   
class Prediction(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    #foreign key
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))

    #spécifier la relation entre les deux classes
    email = db.relationship("Email",back_populates="prediction",uselist=False)

    def __repr__(self):
        return f"Prediction('{self.id}','{self.categorie_id}')" #afficher les categories et leur libelle

class ChoixUtilisateur(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    #foreign key
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))
    #spécifier la relation entre les deux classes
    email = db.relationship("Email",back_populates="choix_utilisateur",uselist = False)

    def __repr__(self):
        return f"Choix Utilisateur('{self.id}','{self.categorie_id}')" #afficher les categories et leur libelle

     