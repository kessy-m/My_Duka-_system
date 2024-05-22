import psycopg2

host= 'localhost'
database='myduka'
user= 'postgres'
password= '12345'
port= '5432'

# connecting to the postgreSQL database
conn=psycopg2.connect(
host= 'localhost',
database='myduka',
user= 'postgres',
password= '12345',
port= 5432
)
# open a cursor to perform database operation

cur = conn.cursor()

# def get_products():
#     cur.execute('select * from products;')
#     prods=cur.fetchall()
#     for i in prods:
#         print(i)
# get_products



# get_products

def get_data(table_name):
    cur.execute(f'select * from {table_name}')
    data = cur.fetchall()
    return data

# products=get_data('products')
# print(products)
# get_data('sales')


# insert values

def insert_products(values):
    cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)",values)
    conn.commit()

product_value=('boots', 3000, 5000, 10)
# insert_products(product_value)
get_data('products')


# insert sales
def insert_sales(values):
    cur.execute("insert into sales(pid,quantity,created_at)values(%s,%s,now())",values)
    conn.commit()


# create a function to display profit per product ()
def total_profit():
    myprofit='select p.name, sum(((selling_price-buying_price) *quantity)) as profit from products as p join sales as s on s.pid=p.id group by p.name ;'
    cur.execute(myprofit)
    data=cur.fetchall()
    return data



#CREATE A FUNCTION TO DISPLAY PROFIT PER DAY
def day_profit():
    d_profit='select date(created_at) as day, sum((selling_price-buying_price)*quantity) as profit from products as p join sales as s on s.pid=p.id group by day order by day;'
    cur.execute(d_profit)
    data=cur.fetchall()
    return data

# create a function to display sales per product
def total_sales():
    t_sales="select p.name ,sum(selling_price*quantity) as result from products as p join sales as s on s.pid=p.id group by p.name;"
    cur.execute(t_sales)
    data=cur.fetchall()
    return data


# create a function to display sales per day
def day_sales():
    d_sales='select date(created_at) as day, sum((selling_price*quantity))as profit from products as p join sales as s on s.pid=p.id group by day;'
    cur.execute(d_sales)
    data=cur.fetchall()
    return (data)


# insert user
def insert_user(values):
   query='insert INTO users (full_name, email, password) values(%s,%s,%s);'
   cur.execute(query,values)
   conn.commit()

# check email
def check_email(email):
       query='select * from users where email=%s '
       cur.execute(query,(email,))
       data=cur.fetchone()
       return data

#  check credentials
def check_email_exist(email):
    query='select * from users where email=%s'
    cur.execute(query,(email,))
    data=cur.fetchall()
    return data

#check if email and password exists
def check_email_pass(email,password):
    query='select * from users where email=%s and password=%s'
    cur.execute(query,(email,password,))
    data=cur.fetchall()
    return data