from flask_app import app, db, bcrypt
import pytest
from random import randint
import requests
from flask_app.modelsdatabase import User, Email, Prediction, ChoixUtilisateur, Categorie

@pytest.fixture
def client():
    app.config["TESTING"]= True
    app.config['SECRET_KEY'] = '606c4261b169756bba33c5e36525d288'
    with app.test_client() as client:
        yield client 
        
def test_home(client):
    url = "/home"
    res = client.get(url)
    assert res.status_code == 200

def test_register(client):
    url = "/register"
    res = client.get(url)
    assert res.status_code == 200

def test_logout(client):
    url = "/logout"
    res = client.get(url)
    assert res.status_code == 302

def test_login(client):
    url = "/login"
    res = client.get(url)
    assert res.status_code == 200

def test_classeremail(client):
    url = "/email/new"
    res = client.get(url)
    #assert res.status_code == 200
    assert res.status_code == 302

#test de la connexion 
def test_connexion():
    user = User.query.filter_by(login_email= 'admin@blog.com').first()
    assert bcrypt.check_password_hash(user.mot_de_passe, 'admin') == True


#test de la requête api
def test_requestapi():
    res = requests.post("http://23.251.133.90/predict",json = {"text":"api ne fonctionne pas les clients sont furieux."} )
    response = '{"prediction":"communication","status":"prediction_done"}'
    #enlever les caractères de control avec rstrip
    assert res.text.rstrip() == response 

#test base de données 
def test_insert_bdd():
    user_pseudo= 'test'+ str(randint(1,1000))
    user_test = User(pseudo = user_pseudo,login_email= user_pseudo+'@test.com',mot_de_passe='python')
    db.session.add(user_test)
    db.session.commit()
    assert type(User.query.filter_by(login_email = user_pseudo+'@test.com').first()) == type(User())