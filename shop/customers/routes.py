import secrets
import os
from flask import render_template, redirect, request, url_for,flash, session, current_app
from shop import db, app, photos, bcrypt, login_manager
from flask_login import current_user, login_required, logout_user, login_user
from .forms import CustomerRegistrationForm, CustomerLoginForm
from .models import Register

@app.route('/customer/register', methods = ['GET','POST'])
def customer_register():
    form = CustomerRegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,
                            country=form.country.data, city=form.city.data,contact=form.contact.data,
                            address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        db.session.commit()
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        return redirect(url_for('login'))
    return render_template('customer/register.html', form = form)

@app.route('/customer/login', methods = ['GET','POST'])
def customerLogin():
    form = CustomerLoginForm()
    if form.validate_on_submit():
        user = Register.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are logged in now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('home'))
        flash('Password or Email is incorrect, Please try again!', 'danger')
        return redirect(url_for('customerLogin'))

    return render_template('customer/login.html',form = form)
