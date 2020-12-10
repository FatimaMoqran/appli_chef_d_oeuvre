#import de flaskform pour faire un formulaire d'enregistrement
from flask_wtf import FlaskForm
#pour ajouter les champs pour les noms
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
#pour ajouter des validations aux champs requis
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_app.modelsdatabase import User

#formulaire d'enregistrement 
class RegistrationForm(FlaskForm):
    pseudo = StringField('Pseudo',
    #obligation de mettre quelque chose et contrôle de la longueur 
                            validators=[DataRequired(), Length(min=2,max=20)])
                            
    login_email = StringField('Login Email',
                        validators= [DataRequired(), Email()])

    mot_de_passe = PasswordField('Mot de passe', validators = [DataRequired()])
    confirm_mot_de_passe= PasswordField('Confirme Mot de passe',
                                        validators=[DataRequired(), EqualTo('mot_de_passe')])
    submit = SubmitField('Enregistrer')

    #on ajoute une validation error si jamais on se retrouve avec le même pseudo
     
    def validate_pseudo(self, pseudo):
         user = User.query.filter_by(pseudo=pseudo.data).first()
         if user:
             raise ValidationError("Ce login existe déja. Merci de choisir un nouveau login.")

    #on ajoute une validation error si jamais on se retrouve avec le même pseudo
    def validate_login_email(self, login_email):
         user = User.query.filter_by(login_email=login_email.data).first()
         if user:
             raise ValidationError("Ce login_email existe déja. Merci d'en choisir un nouveau.")

#formulaire pour se connecter
class LoginForm(FlaskForm):

    login_email = StringField('Login Email',
                        validators= [DataRequired(), Email()])

    mot_de_passe = PasswordField('Mot de passe', validators = [DataRequired()])
    remember = BooleanField('Se souvenir de moi')
    submit = SubmitField('Connection')

#formulaire pour entrer un email
class PostForm(FlaskForm):
    texte = TextAreaField('Email', validators = [DataRequired()])
    submit = SubmitField('Classer')