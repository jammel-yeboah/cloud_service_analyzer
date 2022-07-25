

import os

from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login      import LoginManager
from flask_bcrypt     import Bcrypt
from decouple import config as cg
from flask_migrate import Migrate

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('app.config.Config')

#recaptcha
app.config['RECAPTCHA_PUBLIC_KEY']=cg('RECAPTCHA_PUBLIC_KEY', default='None')
app.config['RECAPTCHA_PRIVATE_KEY']=cg('RECAPTCHA_PRIVATE_KEY', default='None')


db = SQLAlchemy  (app) # flask-sqlalchemy
bc = Bcrypt      (app) # flask-bcrypt

migrate= Migrate(app, db)

lm = LoginManager(   ) # flask-loginmanager
lm.init_app(app)       # init the login manager

# Setup database
@app.before_first_request
def initialize_database():
    db.create_all()

# Import routing, models and Start the App
from app import views, models
from app.apis import gcp, aws, azure, cloud_map
