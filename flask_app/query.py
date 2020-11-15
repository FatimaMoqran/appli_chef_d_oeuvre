from flask_app import db
from modelsdatabase  import User, Email, Categorie, Prediction, ChoixUtilisateur

emails = Email.query.all()
print(emails)
