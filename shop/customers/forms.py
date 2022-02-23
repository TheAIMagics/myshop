from wtforms import Form,StringField, TextAreaField, SubmitField, PasswordField,validators, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm
from .models import Register

class CustomerRegistrationForm(FlaskForm):
    name = StringField('Name: ')
    username = StringField('Username: ', [validators.DataRequired()])
    email = StringField("Email: ", [validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired(),validators.EqualTo('confirm')])
    confirm = PasswordField("Confirm password:", [validators.DataRequired()])
    country = StringField('Country: ', [validators.DataRequired()])
    state = StringField('State: ', [validators.DataRequired()])
    city = StringField('City: ',[validators.DataRequired()])
    contact = StringField('Contact: ',[validators.DataRequired()])
    address = StringField('Address: ',[validators.DataRequired()])
    zipcode = StringField('Zip Code: ',[validators.DataRequired()])

    profile = FileField('Profile', validators=[FileAllowed(['jpg','png','jpeg','gif'])])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if Register.query.filter_by( username = username.data).first():
            raise ValidationError('This username already exists')

    def validate_email(self, email):
        if Register.query.filter_by( username = email.data).first():
            raise ValidationError('This email already exists')

class CustomerLoginForm(FlaskForm):
    email = StringField("Email: ", [validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])
    submit = SubmitField('Login')



