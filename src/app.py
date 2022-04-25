from flask            import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login      import LoginManager


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



# Logout user
@app.route('/logout.html')
def logout():
    #logout_user()
    return redirect(url_for('index'))