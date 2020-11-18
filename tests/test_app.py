from flask_app import db 
from flask_app.modelsdatabase import User

def test_register(app, client):
    res = client.get("/register")
    assert res.status_code == 200
    expected = 

    assert 
