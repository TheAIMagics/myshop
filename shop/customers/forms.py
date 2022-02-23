from wtforms import Form,StringField, TextAreaField, SubmitField, PasswordField,validators
from flask_wtf.file import FileField, FileAllowed, FileRequired

class CustomerRegistrationForm(Form):
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