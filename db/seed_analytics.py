def seed_analytics(db):
    
    db.run("DROP TABLE IF EXISTS dim_customers;")
    db.run("DROP TABLE IF EXISTS dim_products;")
    db.run("DROP TABLE IF EXISTS dim_date;")
    db.run("DROP TABLE IF EXISTS fact_orders;")

    create_dim_customers(db)
    create_dim_products(db)
    create_dim_date(db)
    create_fact_orders(db)


def create_dim_customers(db):
    return db.run("""CREATE TABLE dim_customers (
                  customer_id INT PRIMARY KEY,
                  name VARHCHAR(255),
                  age INT,
                  city VARCHAR(255)
                  );""")

def create_dim_products(db):
    return db.run("""CREATE TABLE dim_products (
                  product_id INT PRIMARY KEY,
                  product_name VARCHAR(255),
                  price INT,
                  ):
                """)

def create_dim_date(db):
    return db.run("""CREATE TABLE dim_date (
                  date_id INT PRIMARY KEY AUTO_INCREMENT,
                  date TIMESTAMP,
                  year INT,
                  month INT,
                  day INT);""")

def create_fact_orders(db):
    return db.run("""CREATE TABLE fact_orders (
                  order_id INT PRIMARY KEY,
                  product_id INT,
                  customer_id INT,
                  date_id INT,
                  price INT,
                  satisfaction_rating INT,
                  FOREIGN KEY (product_id) dim_products(product_id),
                  FOREIGN KEY (customer_id) dim_customers(customer_id),
                  FOREIGN KEY (date_id) dim_date(date_id)
                  );""")
