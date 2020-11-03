#import de flaskform pour faire un formulaire d'enregistrement
from flask_wtf import FlaskForm
#pour ajouter les champs pour les noms
from wtforms import StringField, PasswordField, SubmitField, BooleanField
#pour ajouter des validations aux champs requis
from wtforms.validators import DataRequired, Length, Email, EqualTo

#formulaire d'enregistrement 
class RegistrationForm(FlaskForm):
    username = StringField('Username',
    #obligation de mettre quelque chose et contrôle de la longueur 
                            validators=[DataRequired(), Length(min=2,max=20)])

    email = StringField('Email',
                        validators= [DataRequired(), Email()])

    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

#formulaire pour se connecter
class LoginForm(FlaskForm):

    email = StringField('Email',
                        validators= [DataRequired(), Email()])

    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')