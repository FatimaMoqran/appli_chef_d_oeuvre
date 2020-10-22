
from flask import render_template
from flask_app import app
from flask_app.modelsdatabase import User, Email

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/administrateur')
def admin():
    return render_template('administrateur.html')

