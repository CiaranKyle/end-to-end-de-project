def seed(db, customers, product):
    '''Seeds database'''
    db.run("DROP TABLE IF EXISTS customers;")
    db.run("DROP TABLE IF EXISTS products;")
    create_customers(db)
    create_products(db)

    for row in customers['data']:
        items_bought_string = ', '.join(row['items_bought'])
        db.run('''INSERT INTO customers
            (customer_name, age, items_bought, satisfaction_rating)
            VALUES 
            (:first_name, :age, :items_bought, :satisfaction_rating);''',
            first_name = row['first_name'], age = row['age'],
            items_bought = items_bought_string,
            satisfaction_rating = row['satisfaction_rating']
            )
        
    for row in product['products']:
        db.run('''INSERT INTO productsc
               (product_name, price)
               VALUES
               (:product_name, :price);''',
               product_name = row['product_name'], price = row['price'])
    

def create_customers(db):
    '''Items bought will eventually reference product_id :)'''
    return db.run('''CREATE TABLE customers (
                  customer_id SERIAL PRIMARY KEY,
                  customer_name VARCHAR(40) NOT NULL,
                  age INT NOT NULL,
                  items_bought VARCHAR(200) NOT NULL,
                  satisfaction_rating INT NOT NULL
                  )''')

def create_products(db):
    return db.run('''CREATE TABLE products (
                  product_id SERIAL PRIMARY KEY,
                  product_name VARCHAR(40) NOT NULL,
                  price INT NOT NULL
                  )''')