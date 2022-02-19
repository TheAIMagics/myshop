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

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template('products/updatebrand.html', title='UPdate brand',brands='brands',updatebrand=updatebrand)

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

@app.route('/updatecategory/<int:id>',methods=['GET','POST'])
def updatecategory(id):
    updatecategory = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method =="POST":
        updatecategory.name = category
        flash(f'The brand {updatecategory.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('products/updatebrand.html', title='UPdate brand',updatecategory=updatecategory)

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

@app.route('/updateproduct/<int:id>', methods = ['GET', 'POST'])
def updateproduct(id):
    brands = Brand.query.all()
    categories = Category.query.all()
    product = Addproduct.query.get_or_404(id)
    print(product.price)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = AddproductsForm(request.form)
    if request.method == 'POST':
        product.name = form.name.data
        product.price = form.price.data
        product.stock = form.stock.data
        product.discount = form.discount.data
        product.description = form.description.data
        product.colors = form.colors.data
        product.brand_id = brand
        product.category_id = category
        db.session.commit()
        flash("Product has been updated successfully", 'success')
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.stock.data = product.stock
    form.discount.data = product.discount
    form.description.data = product.description
    form.colors.data = product.colors
    return render_template('products/updateproduct.html', title = 'Update Product', form = form,brands = brands, categories=categories,
                           product = product)