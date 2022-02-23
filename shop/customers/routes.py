import secrets
import os
from flask import render_template, redirect, request, url_for,flash, session, current_app
from shop import db, app, photos, bcrypt
from .forms import CustomerRegistrationForm
from .models import Register

@app.route('/customer/register', methods = ['GET','POST'])
def customer_register():
    form = CustomerRegistrationForm(request.form)
    if request.method == 'POST':
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,
                            country=form.country.data, city=form.city.data,contact=form.contact.data,
                            address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        db.session.commit()
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        return redirect(url_for('login'))
    return render_template('customer/register.html', form = form)

