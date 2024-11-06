def seed(db, customers, product):
    '''Seeds database'''

    db.run("DROP TABLE IF EXISTS orders;")
    db.run("DROP TABLE IF EXISTS products;")
    db.run("DROP TABLE IF EXISTS customers;")

    create_customers(db)
    create_products(db)
    create_orders_table(db)

    for row in customers['data']:
        db.run('''INSERT INTO customers
            (first_name, last_name, age, satisfaction_rating,
            date_of_purchase, city)
            VALUES 
            (:first_name, :last_name, :age, :satisfaction_rating,
            :date_of_purchase, :city);''',
            first_name = row['first_name'], last_name = row['last_name'],
            age = row['age'],
            satisfaction_rating = row['satisfaction_rating'],
            date_of_purchase = row['date_of_purchase'],
            city = row['city']
            )
        
    for row in product['products']:
        db.run('''INSERT INTO products
               (product_name, price)
               VALUES
               (:product_name, :price);''',
               product_name = row['product_name'], price = row['price'])
    
    count = 0
    for row in customers['data']:
        count += 1
        for item in row['items_bought']:
            db.run('''INSERT INTO orders 
                   (product_id, customer_id, date)
                   VALUES (
                   (SELECT product_id FROM products
                    WHERE product_name = :product_name), 
                   :customer_id, :date)''',
                   product_name=item,
                   customer_id=count, 
                   date=row['date_of_purchase'])

def create_customers(db):
    return db.run('''CREATE TABLE customers (
                  customer_id SERIAL PRIMARY KEY,
                  first_name VARCHAR(40) NOT NULL,
                  last_name VARCHAR(40) NOT NULL,
                  age INT NOT NULL,
                  satisfaction_rating INT NOT NULL,
                  date_of_purchase VARCHAR(32) NOT NULL,
                  city VARCHAR(32) NOT NULL
                  )''')

def create_products(db):
    return db.run('''CREATE TABLE products (
                  product_id SERIAL PRIMARY KEY,
                  product_name VARCHAR(40) NOT NULL,
                  price INT NOT NULL
                  )''')

def create_orders_table(db):
    return db.run("""CREATE TABLE orders (
                  order_id SERIAL PRIMARY KEY, 
                  product_id INT NOT NULL,
                  customer_id INT NOT NULL,
                  date VARCHAR(16),
                  FOREIGN KEY (product_id) REFERENCES products(product_id),
                  FOREIGN KEY (customer_id) REFERENCES customers(customer_id));""")