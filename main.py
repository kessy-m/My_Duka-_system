from flask import Flask,render_template,request,redirect,url_for,flash,session
from database import get_data,insert_products,insert_sales,total_profit,day_profit,total_sales,day_sales,insert_user,check_email,check_email_exist,check_email_pass
# flask instance

app=Flask(__name__)
app.secret_key='cupcake'


# check login
def check_login():
    if 'email' not in session:
        return redirect(url_for('login'))
    


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
    if 'email' not in session:
        return redirect(url_for('login'))
    products=get_data('products')
    print(products)
    return render_template('products.html',prods=products)



# CREATE ONE FOR SALES
@app.route('/sales')
def sales():
    if 'email' not in session:
        return redirect(url_for('login'))
    sales=get_data('sales')
    prods=get_data('products')
    print(sales)
    return render_template('sales.html',mysales=sales,myprods=prods)


# CREATE ONE FOR DASHBOARD
@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))
    profit=total_profit()
    name_profit=[]
    value_profit=[]
    for i in profit:
        name_profit.append(str(i[0]))
        value_profit.append(float(i[1]))
        
        
# create profit per day
    dayprofit=day_profit()
    days=[]
    d_profit=[]
    for d in dayprofit:
        days.append(str(d[0]))
        d_profit.append(float(d[1]))

# create sales per product
    mysales=total_sales()
    sales=[]
    sales_products=[]
    for s in mysales:
        sales.append(str(s[0]))
        sales_products.append(float(s[1]))

 # create sales per day
    allsales=day_sales()
    s_day=[]   
    t_sales=[]   
    for w in allsales:
        s_day.append(str(w[0]))  
        t_sales.append(float(w[1]))
    return render_template('dashboard.html',profit=value_profit,name=name_profit,days=days,p_d=d_profit,sales1=sales,s_p=sales_products,daysales=s_day,totalsales=t_sales)




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



# create a login route
@app.route('/login', methods=['POST','GET'] )
def login():
    # get form data
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']

        #  check email exists
        ch_email=check_email_exist(email)
        if len(ch_email)<1:
            flash('email does not exist')
            return redirect(url_for('register'))
        else:
            ch_pass=check_email_pass(email,password)
            if len(ch_pass)<1:
                flash('try again')
            else:
                session['email']=email
                flash('login succesfully')    
                return redirect(url_for('dashboard'))
    return render_template('login.html')

# create a log out route
@app.route('/log_out')
def log_out():
    session.pop('email',None)
    flash('logout successfully',)
    return redirect(url_for('login'))



# create a register route 
@app.route('/register', methods=['POST','GET'])
def register():
    if request.method=="POST":
        f_name=request.form['full_name']
        email=request.form['email']
        password=request.form['password']
# insert user
        ch_email=check_email(email)
        if len(ch_email)<1:
            new_user=(f_name,email,password)
            insert_user(new_user)
            flash('register')
            return redirect(url_for('login'))
        else:
            flash('email exist')
    return render_template('register.html')



# app.run(debug=True)


