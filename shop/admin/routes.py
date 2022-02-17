from flask import render_template, url_for, redirect, request, flash
from shop import db, app, bcrypt
from .forms import RegistrationForm
from .models import User

@app.route('/')
def home():
    return render_template('admin/index.html', title ='Admin Page')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name = form.name.data, username = form.username.data,email= form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"{form.name.data} ! Registered successfully", 'success')
        return redirect(url_for('home'))
    return render_template('admin/register.html', title = 'Register user', form = form)
