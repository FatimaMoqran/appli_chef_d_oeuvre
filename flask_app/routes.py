
from flask import render_template, flash, redirect, url_for
from flask_app import app
from flask_app.forms import RegistrationForm, LoginForm
from flask_app.modelsdatabase import User, Email


@app.route('/')
@app.route('/home',methods=['POST'])
def home():
    print('ok')
    return render_template('home.html')

@app.route('/administrateur')
def admin():
    return render_template('administrateur.html', title= 'Page Administrateur')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # flash message pour nous dire si c'est validé ou pas
    if form.validate_on_submit():
        flash(f'Le compte est crée pour {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #simule un  une connection validé
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Vous êtes bien connecté', 'success')
            return redirect(url_for('home'))
        else:
            flash('La connection a été refusé. Veuillez vérifier votre email et mot de passe','danger')
    return render_template('login.html', title='Login', form=form)
   