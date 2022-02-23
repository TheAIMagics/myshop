import secrets
import os
from flask import render_template, redirect, request, url_for,flash, session, current_app
from shop import db, app, photos
from .forms import CustomerRegistrationForm

@app.route('/customer/register', methods = ['GET','POST'])
def customer_register():
    form = CustomerRegistrationForm(request.form)
    return render_template('customer/register.html', form = form)

