
from flask_app import app

#permet de runner l'application directement dans python
if __name__ == '__main__':
    app.config['SECRET_KEY'] = '606c4261b169756bba33c5e36525d288'
    app.run(debug=True)
