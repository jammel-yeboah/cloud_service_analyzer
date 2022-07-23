# -*- encoding: utf-8 -*-

from random import choices
from flask_wtf          import FlaskForm, RecaptchaField
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])

class RegisterForm(FlaskForm):
	name        = StringField  (u'Name'      )
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])
	email       = StringField  (u'Email'     , validators=[DataRequired(), Email()])

class cloudForm(FlaskForm):
    category= SelectField('Category', choices=[], default=0)
    type= SelectField('Type', choices=[])
    region= SelectField('Region', choices=[
						("eastus","(US) East US"),
						("eastus2","(US) East US 2"),
						("southcentralus","(US) South Central US"),
						("westus2","(US) West US 2"),
						("westus3","(US) West US 3"),
						("australiaeast","(Asia Pacific) Australia East"),
						("southeastasia","(Asia Pacific) Southeast Asia"),
						("northeurope","(Europe) North Europe"),
						("swedencentral","(Europe) Sweden Central"),
						("uksouth","(Europe) UK South"),
						("westeurope","(Europe) West Europe"),
						("centralus","(US) Central US"),
						("northcentralus","(US) North Central US"),
						("westus","(US) West US"),
						("southafricanorth","(Africa) South Africa North"),
						("centralindia","(Asia Pacific) Central India"),
						("eastasia","(Asia Pacific) East Asia"),
						("japaneast","(Asia Pacific) Japan East"),
						("jioindiawest","(Asia Pacific) Jio India West"),
						("koreacentral","(Asia Pacific) Korea Central"),
						("canadacentral","(Canada) Canada Central"),
						("francecentral","(Europe) France Central"),
						("germanywestcentral","(Europe) Germany West Central"),
						("norwayeast","(Europe) Norway East"),
						("switzerlandnorth","(Europe) Switzerland North"),
						("uaenorth","(Middle East) UAE North"),
						("brazilsouth","(South America) Brazil South"),
						("centralusstage","(US) Central US (Stage)"),
						("eastusstage","(US) East US (Stage)"),
						("eastus2stage","(US) East US 2 (Stage)"),
						("northcentralusstage","(US) North Central US (Stage)"),
						("southcentralusstage","(US) South Central US (Stage)"),
						("westusstage","(US) West US (Stage)"),
						("westus2stage","(US) West US 2 (Stage)"),
						("asia","Asia"),
						("asiapacific","Asia Pacific"),
						("australia","Australia"),
						("brazil","Brazil"),
						("canada","Canada"),
						("europe","Europe"),
						("france","France"),
						("germany","Germany"),
						("global","Global"),
						("india","India"),
						("japan","Japan"),
						("korea","Korea"),
						("norway","Norway"),
						("southafrica","South Africa"),
						("switzerland","Switzerland"),
						("uae","United Arab Emirates"),
						("uk","United Kingdom"),
						("unitedstates","United States"),
						("unitedstateseuap","United States EUAP"),
						("eastasiastage","(Asia Pacific) East Asia (Stage)"),
						("southeastasiastage","(Asia Pacific) Southeast Asia (Stage)"),
						("centraluseuap","(US) Central US EUAP"),
						("eastus2euap","(US) East US 2 EUAP"),
						("westcentralus","(US) West Central US"),
						("southafricawest","(Africa) South Africa West"),
						("australiacentral","(Asia Pacific) Australia Central"),
						("australiacentral2","(Asia Pacific) Australia Central 2"),
						("australiasoutheast","Canada"),
						("japanwest","(Asia Pacific) Japan West"),
						("jioindiacentral","(Asia Pacific) Jio India Central"),
						("koreasouth","(Asia Pacific) Korea South"),
						("southindia","(Asia Pacific) South India"),
						("westindia","(Asia Pacific) West India"),
						("canadaeast","(Canada) Canada East"),
						("francesouth","(Europe) France South"),
						("germanynorth","(Europe) Germany North"),
						("norwaywest","(Europe) Norway West"),
						("switzerlandwest","(Europe) Switzerland West"),
						("ukwest","(Europe) UK West"),
						("uaecentral","(Middle East) UAE Central"),
						("brazilsoutheast","(South America) Brazil Southeast")])
    #recaptcha = RecaptchaField()