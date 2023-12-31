from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'secretKey'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///file.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes, models

