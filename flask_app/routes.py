
from flask import render_template, flash, redirect, url_for, request
from flask_app import app, db , bcrypt
from flask_app.forms import RegistrationForm, LoginForm, PostForm
from flask_app.modelsdatabase import User, Email, Prediction, ChoixUtilisateur, Categorie
from flask_login import login_user, current_user, logout_user, login_required
from flask_app.classify import classify

@app.route('/')
@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/administrateur',methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':

        emails = Email.query.all()
        predictions = Prediction.query.all()
        choix_utilisateur = ChoixUtilisateur.query.all()
        categories = Categorie.query.all()
        prediction_ok = 0
        data = []
        #recupère chaque element des tuples renvoyés par la base de donnée
        for email, prediction, choix_utilisateur in zip(emails, predictions,choix_utilisateur):
            if prediction.id == choix_utilisateur.id and prediction.categorie_id == choix_utilisateur.categorie_id:
                prediction_ok +=1 
        #recupère quand les predictions ne sont pas ok les élements que je vais afficher pour l'administrateur
            else:
                tmp = []
                tmp.append(email.texte)
                tmp.append(prediction.categorie_id)
                tmp.append(choix_utilisateur.categorie_id)
                data.append(tmp)

        taux = round((prediction_ok/ db.session.query(Email.texte).count())*100)
        nb_elements = db.session.query(Email.texte).count()
        print("taux de prediction correctes %s"%(taux))
        
        
        return render_template('administrateur.html', title= 'Page Administrateur', data = data, taux = taux, nb_elements = nb_elements )
    else:
        return 'Erreur permission denied'

@app.route("/register", methods=['GET', 'POST'])
def register():
    #si on est déja authentifié on n'a pas accès à la page enregistrement
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    # flash message pour nous dire si c'est validé ou pas
    if form.validate_on_submit():
        #crypter le mot de passe 
        hashed_password = bcrypt.generate_password_hash(form.mot_de_passe.data).decode('utf-8')
        #on crée une variable user
        user = User(pseudo=form.pseudo.data, login_email=form.login_email.data, mot_de_passe=hashed_password)
        #on l'enregistre dans la base de données 
        db.session.add(user)
        db.session.commit()

        flash(f'Votre compte a été crée! Vous pouvez maintenant vous connecter', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    #si on est déja authentifié on n'a pas accès à la page connexion
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login_email= form.login_email.data).first()
        if user and bcrypt.check_password_hash(user.mot_de_passe, form.mot_de_passe.data):
            login_user(user, remember= form.remember.data)
            if user.login_email == 'admin@blog.com':
                return redirect(url_for('admin'), code = 307)
            #nous permet d'aller vers la page account que lorsque nous sommes connecté
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('La connection a été refusé. Veuillez vérifier votre email et mot de passe','danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))  

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

#nouvelle route pour poster les emails(il faut être connecté)
@app.route('/email/new', methods = ['GET', 'POST'])
@login_required
def classer_email():
    form = PostForm()
    if form.validate_on_submit():
        if request.method == "POST":
            texte = request.form['texte']
            print(texte)
            response = classify(texte)
            if response["status"] == "prediction_done": 
                #print('je vais dans le prédiction')
                #enregistrer la prediction et le texte 
                
                prediction = Prediction(categorie_id = response['prediction'])
                db.session.add(prediction)
                db.session.commit()
                email = Email(texte =texte,prediction_id= prediction.id, sender = current_user )
                db.session.add(email)
                db.session.commit()
                return render_template('prediction.html',title= 'prediction', response=response, form='form')
        else :
            render_template('classer_email.html', title='Classer votre email', form=form)
    return render_template('classer_email.html', title='Classer votre email', form=form)

@app.route('/enregistrer_email', methods = ['GET','POST'])       
def enregistrer_email():
    form = PostForm()
    if request.method == "POST":
        #enregistrer le choix
        choix_utilisateur = ChoixUtilisateur(categorie_id=request.form['select_categorie'])
        db.session.add(choix_utilisateur)
        db.session.commit()
        email= db.session.query(Email).order_by(Email.id.desc()).first()
        email.choix_utilisateur= choix_utilisateur 
        db.session.commit()
        flash('votre email a été classé','succes')
    return render_template('home.html', title='Classer votre email', form=form)

