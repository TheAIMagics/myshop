from flask import render_template, redirect, request, url_for,flash, session
from shop import db, app
from .models import Brand, Category
from .forms import AddproductsForm

@app.route('/')
def home():
    return "Home Page"

@app.route('/addbrand', methods = ['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name = getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f"Brand { getbrand } added to your database",'success')
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brands = 'brands')


@app.route('/addcategory', methods = ['GET', 'POST'])
def addcategory():
    if request.method == "POST":
        getcategory= request.form.get('category')
        print(getcategory)
        category = Category(name = getcategory)
        db.session.add(category)
        db.session.commit()
        flash(f"Category {getcategory} added to your database",'success')
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html')

@app.route('/addproduct', methods = ['GET', 'POST'])
def addproduct():
    form = AddproductsForm(request.form)
    return render_template('products/addproduct.html', title="Add Product", form = form)