import secrets
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from shop.admin import routes