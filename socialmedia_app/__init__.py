from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# Create the app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Bcrypt
bcrypt = Bcrypt(app)

# Import the routes
from socialmedia_app import routes