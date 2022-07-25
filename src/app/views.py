
# Python modules
import os, logging
from ossaudiodev import SNDCTL_DSP_BIND_CHANNEL
import sys
import os
import pandas as pd


# Flask modules
from flask               import jsonify, render_template, request, url_for, redirect, send_from_directory, flash
from requests import session
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2              import TemplateNotFound
from flask               import session
from flask_bootstrap     import Bootstrap

# App modules
from app        import app, lm, db, bc
from app.models import Users, Reports
from app.forms  import LoginForm, RegisterForm, cloudForm
from app.apis import gcp, aws, azure, cloud_map

Bootstrap(app)

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
        filter= cloud_map.filter_options()
        form.category.choices= filter.get_categories()
        form.type.choices= filter.get_service_type()
        return render_template('cloud_form.html', form=form)
    else:
        if current_user.is_authenticated:
            user= current_user.id
            report= Reports(
                user_id= user,
                serviceCategory= form.category.data,
                serviceType=form.type.data,
                serviceRegion=form.region.data,
                instances=form.instances.data,
                machineFamily=form.machineFamily.data,
                infrastructureType=form.infrastructureType.data)

            db.session.add(report) #add report to database
            db.session.commit()

        session['cloud_form_data']= {'category':form.category.data,'type': form.type.data,'region': form.region.data}
        return redirect(url_for('display_results'))

@app.route('/service_types/<category>')
def service_types(category):
    filter= cloud_map.filter_options()
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
    filter= cloud_map.filter_options()
    products= filter.get_products(form_data['category'], form_data['type'])
    gcp_res= gcp.get_gcp_info(products['gcp'])
    aws_res= aws.get_aws_info(products['aws'], region)
    azure_res= azure.get_azure_info(products['azure'], region, form_data['category']) #azure uses identical category namings so adding category will make api query faster
    results={}
    #dictionary where keys are labels and values are lists of info by gc,aws,azure
    for key in gcp_res: results[key]= [gcp_res[key], aws_res[key], azure_res[key]] #all dict keys are the same
    print(results)
    return render_template('display_results.html', results=results)

@app.route('/reports.html')
def reports():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    userReports= Reports.query.filter_by(user_id= current_user.id).all()
    return render_template('reports.html', userReports=userReports)

@app.route('/more_info.html', methods=['GET', 'POST'])
def more_info():
    if request.method== 'POST': return redirect(url_for('more_info'))
    else: return render_template('more_info.html')


@app.route('/viewReport/<int:reportId>', methods=['POST'])
def viewReport(reportId):
    if request.method== "POST":
        report= Reports.query.get_or_404(reportId)
        filter= cloud_map.filter_options()
        products= filter.get_products(report.serviceCategory, report.serviceType)
        gcp_res= gcp.get_gcp_info(products['gcp'])
        aws_res= aws.get_aws_info(products['aws'], report.serviceRegion)
        azure_res= azure.get_azure_info(products['azure'], report.serviceRegion, report.serviceCategory) #azure uses identical category namings so adding category will make api query faster
        results={}
        #dictionary where keys are labels and values are lists of info by gc,aws,azure
        for key in gcp_res: results[key]= [gcp_res[key], aws_res[key], azure_res[key]] #all dict keys are the same
        return render_template('display_results.html', results=results)
    else: return redirect(url_for('reports'))


@app.route('/deleteReport/<reportId>', methods=['GET', 'POST'])
def deleteReport(reportId):
    if request.method== "POST":
        report_to_del= Reports.query.get_or_404(reportId)
        try:
            db.session.delete(report_to_del)
            db.session.commit()
            return redirect(url_for('reports'))
        except:
            flash("There was a problem deleting report. Please try again.")
            return redirect(url_for('reports'))
    else: redirect(url_for('reports'))