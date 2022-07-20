
# Python modules
import os, logging
import sys
import os
import pandas as pd

# Flask modules
from flask               import jsonify, render_template, request, url_for, redirect, send_from_directory
from requests import session
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2              import TemplateNotFound
from flask               import session

# App modules
from app        import app, lm, db, bc
from app.models import Users
from app.forms  import LoginForm, RegisterForm, cloudForm
from app.apis import gcp, aws, azure
# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Logout user
@app.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Register a new user
@app.route('/register.html', methods=['GET', 'POST'])
def register():

    # declare the Registration Form
    form = RegisterForm(request.form)

    msg     = None
    success = False

    if request.method == 'GET':

        return render_template( 'register.html', form=form, msg=msg )

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        email    = request.form.get('email'   , '', type=str)

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = Users.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'

        else:

            pw_hash = bc.generate_password_hash(password)

            user = Users(username, email, pw_hash)

            user.save()

            msg     = 'User created, please <a href="' + url_for('login') + '">login</a>'
            success = True

    else:
        msg = 'Input error'

    return render_template( '/register.html', form=form, msg=msg, success=success )

# Authenticate user
@app.route('/login.html', methods=['GET', 'POST'])
def login():

    # Declare the login form
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        if user:

            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user"

    return render_template( 'login.html', form=form, msg=msg )

# App main route + generic routing
@app.route('/')
def index():
    return render_template('index.html')

# Return sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')

#Cloud pricing analyzer form
@app.route('/cloud_form.html', methods=['GET', 'POST'])
def cloud_form():
    form= cloudForm()
    if request.method == 'GET':
        filter= filter_options()
        form.category.choices= filter.get_categories()
        form.type.choices= filter.get_service_type()
        return render_template('cloud_form.html', form=form)
    session['cloud_form_data']= {'category':form.category.data,'type': form.type.data,'region': form.region.data}
    return redirect(url_for('display_results'))

class filter_options:
    def __init__(self):
        self.df= pd.read_excel("apis/cmap_sheet.xlsx", "Sheet1")

    def get_categories(self): #returns a list of cloud categories to be listed on select menu on forms page
        items= self.df['Service_category'].unique()
        results= [(item, item) for item in items] ##flask wtf requires tuples of data and id
        return results

    def get_service_type(self, category=None):
        if category is None: items= self.df['Service_type'].unique()
        else: items= self.df.loc[self.df['Service_category'] == category, 'Service_type'].unique()
        results= [(item, item) for item in items] ##flask wtf requires tuples of data and id
        return results

    def get_products(self, category, type):
        res= (self.df.query('Service_category== @category and Service_type== @type')).to_dict('list')
        products= {'gcp': res['gcp_offering'][0].split(',')[0],
                    'aws': res['aws_offering'][0].split(',')[0],
                    'azure': res['azure_offering'][0].split(',')[0]}
        return products


@app.route('/service_types/<category>')
def service_types(category):
    filter= filter_options()
    service_types= filter.get_service_type(category)
    service_typeArr= []

    for tup in service_types:
        typeObj= {}
        typeObj['id']= tup[0]
        typeObj['name']= tup[1] ##index 1 and 2 in each tuple matches so tup[0 or 1 ] doesnt matter
        service_typeArr.append(typeObj)
    return jsonify({'service_types': service_typeArr})

@app.route('/display_results.html', methods=['GET', 'POST'])
def display_results():
    form_data= session.get('cloud_form_data')
    region= form_data['region']
    filter= filter_options()
    products= filter.get_products(form_data['category'], form_data['type'])
    gcp_res= gcp.get_gcp_info(products['gcp'])
    aws_res= aws.get_aws_info(products['aws'], region)
    azure_res= azure.get_azure_info(products['azure'], region, form_data['category']) #azure uses identical category namings so adding category will make api query faster
    return render_template('display_results.html', gcp_res=gcp_res, aws_res=aws_res, azure_res=azure_res)
