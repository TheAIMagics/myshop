from flask import render_template, url_for, redirect, request, flash, session
from shop import db, app, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from shop.products.models import Addproduct, Brand, Category

@app.route('/admin')
def admin():
    if 'email' not in session:
        return redirect(url_for('login'))
    products = Addproduct.query.all()
    return render_template('admin/index.html', title ='Admin Page', products= products)

@app.route('/brands')
def brands():
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title ='Brands Page', brands= brands)

@app.route('/category')
def category():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title ='Brands Page', categories= categories)


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name = form.name.data, username = form.username.data,email= form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"{form.name.data} ! Registered successfully", 'success')
        return redirect(url_for('admin'))
    return render_template('admin/register.html', title = 'Register user', form = form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f"Welcome {form.email.data} ! Logged In successfully", 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash("Incorrect Password! Please try again", 'danger')
    return render_template('admin/login.html', form = form , title = 'Login Page')
