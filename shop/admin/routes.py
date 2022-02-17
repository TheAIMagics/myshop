from flask import render_template, url_for, redirect, request
from shop import db, app

@app.route('/')
def home():
    return 'my shop'

@app.route('/register')
def register():
    return render_template('admin/register.html', title = 'Register user')
