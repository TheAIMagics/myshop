import secrets
from flask import render_template, redirect, request, url_for,flash, session
from shop import db, app, photos
from .models import Brand, Category, Addproduct
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
        category = Category(name = getcategory)
        db.session.add(category)
        db.session.commit()
        flash(f"Category {getcategory} added to your database",'success')
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html')

@app.route('/addproduct', methods = ['GET', 'POST'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddproductsForm(request.form)
    if request.method =='POST':
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        description = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name = secrets.token_hex(10) + '.')
        image_2 = photos.save(request.files.get('image_2'),name = secrets.token_hex(10) + '.')
        image_3 = photos.save(request.files.get('image_3'), name = secrets.token_hex(10) + '.')

        addproduct = Addproduct(name=name, price=price, discount=discount, stock=stock, colors=colors,
                                description=description,
                                category_id=category,brand_id=brand, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addproduct)
        db.session.commit()
        flash(f"Product {name} added to your database", 'success')
        return redirect(url_for('admin'))

    return render_template('products/addproduct.html', title="Add Product", form = form,
                           brands = brands, categories = categories)