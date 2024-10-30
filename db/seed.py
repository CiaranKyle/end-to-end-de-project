def seed(db, customers, product):
    '''Seeds database'''
    db.run("DROP TABLE IF EXISTS customers;")
    db.run("DROP TABLE IF EXISTS products;")
    create_customers(db)
    create_products(db)

    for row in customers['data']:
        items_bought_string = ', '.join(row['items_bought'])
        db.run('''INSERT INTO customers
            (first_name, last_name, age, items_bought, satisfaction_rating,
            date_of_purchase, city)
            VALUES 
            (:first_name, :last_name, :age, :items_bought, :satisfaction_rating,
            :date_of_purchase, :city);''',
            first_name = row['first_name'], last_name = row['last_name'],
            age = row['age'], items_bought = items_bought_string,
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
    

def create_customers(db):
    return db.run('''CREATE TABLE customers (
                  customer_id SERIAL PRIMARY KEY,
                  first_name VARCHAR(40) NOT NULL,
                  last_name VARCHAR(40) NOT NULL,
                  age INT NOT NULL,
                  items_bought VARCHAR(200) NOT NULL,
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