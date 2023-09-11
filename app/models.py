#102080131876
from app import db
class Logins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    OrgName = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120))
    def __repr__(self):
        return self.id,'', self.OrgName,'', self.email,'', self.password

    
