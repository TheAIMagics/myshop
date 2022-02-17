from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min = 4 , max=25)])
    email = StringField('Email', [validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Password must match')])
    confirm = PasswordField("Repeast password")

class LoginForm(Form):
    email = StringField('Email', [validators.Email()])
    password = PasswordField('Password',[validators.DataRequired()])

