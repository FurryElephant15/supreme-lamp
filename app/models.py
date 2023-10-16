from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
class Logins(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    OrgName = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120))
    requests = db.relationship('Posts', backref='author')
    def set_password(self, passwordinput):
        self.password= generate_password_hash(passwordinput)
    def check_password(self, passwordinput):
        return check_password_hash(self.password, passwordinput)
    def __repr__(self):
        return self.id,'', self.OrgName,'', self.email,'', self.password
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@login.user_loader
def load_user(id):
    return Logins.query.get(int(id))
class Posts(id):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.String(500), index=True, unique=True)
    city = db.Column(db.String(10), index=True, unique=True)
    ImageA=db.Column(db.LargeBinary)
    ImageB=db.Column(db.LargeBinary)
    ImageC=db.Column(db.LargeBinary)

    
    