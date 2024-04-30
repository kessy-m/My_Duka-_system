from flask import Flask,render_template,request,redirect,url_for,flash
from database import get_data,insert_products,insert_sales
# flask instance

app=Flask(__name__)
app.secret_key='cupcake'

@app.route('/')
def hello():
    return render_template('index.html')



# create another for products
# @app.route('/products')
# def prod():
#     return 'mangoes'



# create another for products render a products.html
@app.route('/products')
def my_products():
    products=get_data('products')
    print(products)
    return render_template('products.html',prods=products)



# CREATE ONE FOR SALES
@app.route('/sales')
def sales():
    sales=get_data('sales')
    prods=get_data('products')
    print(sales)
    return render_template('sales.html',mysales=sales,myprods=prods)


# CREATE ONE FOR DASHBOARD
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# insert products
@app.route('/add_products',methods=['POST','GET'])
def add_prods():
    # request form data
    p_name=request.form['product_name']
    b_price=request.form['Buying_price']
    s_price=request.form['Selling_price']
    stock=request.form['stock_quantity']
    total_products=(p_name,b_price,s_price,stock)

    # insert products
    insert_products(total_products)
    flash(f"{stock}  {p_name} added succesfully")
    return redirect(url_for('my_products'))
    


# make sales
@app.route('/make_sales',methods=['POST','GET'])
def make_sales():
# get form data
    pid=request.form['pid']
    quantity=request.form['stock-quantity']
    mysales=(pid,quantity)

    insert_sales(mysales)
    return redirect(url_for('sales'))

app.run(debug=True)
