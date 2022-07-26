

from app         import db
from flask_login import UserMixin
from datetime import datetime

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))
    #User can have many reports
    reports= db.relationship('Reports', backref='report')

    def __init__(self, user, email, password):
        self.user       = user
        self.password   = password
        self.email      = email

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self

class Reports(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('Users.id'))

    serviceCategory= db.Column(db.String(500))
    serviceType=  db.Column(db.String(500))
    serviceRegion=  db.Column(db.String(500))
    instances=  db.Column(db.String(500))
    machineFamily=  db.Column(db.String(500))
    infrastructureType=  db.Column(db.String(500))
    date= db.Column(db.DateTime, default= datetime.utcnow)