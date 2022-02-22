from flask import render_template, redirect, request, url_for,flash, session, current_app
from shop import db, app, photos
from shop.products.models import Addproduct

def MergeDicts(dict1, dict2):
    if isinstance(dict1,list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    else:
        return False

@app.route('/addcart', methods=['POST','GET'])
def AddCart():
    try:
        product_id = request.form.get('product_id')
        quantity =  int(request.form.get('quantity'))
        colors = request.form.get('colors')
        product = Addproduct.query.filter_by(id= product_id).first()

        if product_id and quantity and colors and product and request.method =='POST':
            DictItems = {product_id: {'name': product.name, 'price': float(product.price), 'discount': product.discount,
                                      'color': colors, 'quantity': quantity, 'image': product.image_1,
                                      'colors': product.colors}}
            if 'Shoppingcart' in session:
                print(session['Shoppingcart'])
                if product_id in session['Shoppingcart']:
                    for key, item in session['Shoppingcart'].items():
                        if int(key) == int(product_id):
                            session.modified = True
                            item['quantity'] += 1
                else:
                    session['Shoppingcart'] = MergeDicts(session['Shoppingcart'], DictItems)
                    return redirect(request.referrer)
            else:
                session['Shoppingcart'] = DictItems
                return redirect(request.referrer)

    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)

@app.route('/carts', methods=['POST','GET'])
def getCart():
    if 'Shoppingcart' not in session:
        return redirect(request.referrer)
    subtotal = 0
    grandtotal = 0
    for key, product in session['Shoppingcart'].items():
        discount = (product['discount']/100)*float(product['price'])
        subtotal += float(product['price']) * int(product['quantity'])
        subtotal -= discount
        tax = ("%.2f" % (.06 * float(subtotal)))
        grandtotal = float("%.2f" % (1.06 * subtotal))
    return render_template('products/carts.html', tax=tax, grandtotal=grandtotal)