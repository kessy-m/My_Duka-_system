import psycopg2

host= 'localhost'
database='myduka'
user= 'postgres'
password= '12345'
port= '5432'

# connecting to the postgreSQL database
conn=psycopg2.connect(
    dbname= 'myduka',
    user= 'postgres',
    password= '12345',
    host= 'localhost',
    port= '5432'
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
    cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)\
                values(%s,%s,%s,%s)",values)
    conn.commit()

product_value=('boots', 3000, 5000, 10)
# insert_products(product_value)
get_data('products')


# insert sales
def insert_sales(values):
    cur.execute("insert into sales(pid,quantity,created_at)values(%s,%s,now())",values)
    conn.commit()









