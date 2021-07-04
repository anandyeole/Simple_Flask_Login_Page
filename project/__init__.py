# importing packages
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, current_user
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

# current directory path
basedir = os.path.abspath(os.path.dirname(__file__))

# Application instance
app = Flask(__name__)

# app secret key
app.config["SECRET_KEY"] = "newkey"

# connect our app with database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)

# don't track every database modification
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

# create instance of db
db = SQLAlchemy(app)
Migrate(app, db)

# Manages login
login_manager = LoginManager()
login_manager.init_app(app)

# whenever login is required and user tries to access the page redirect user to login first
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return userDetails.query.get(user_id)


########################################################################################


# databse structure of userdetails table
class userDetails(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = bcrypt.generate_password_hash(password=password)

    # check password with hashed database password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


# blueprint for routes of auth
from project.auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)
