from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
class Logins(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    OrgName = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120))
    requests = db.relationship('Posts', backref='author', lazy='dynamic')
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
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    description = db.Column(db.String(500), index=True)
    city = db.Column(db.String(10), index=True)
    ImageA=db.Column(db.String(500))
    ImageB=db.Column(db.String(500))
    ImageC=db.Column(db.String(500))
    email = db.Column(db.String(500), index=True, unique=True)
    phone = db.Column(db.String(500), index=True, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey('logins.id'))
    def __repr__(self):
        return "<Post in {}>".format(self.city)


    
    