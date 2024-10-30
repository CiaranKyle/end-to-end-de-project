from db.connection import create_conn, close_db

"""Need to Unnest the data in the customers table. Split out the products and 
orders placed. Then we can make a column in customers table of how much a 
customer has spent to date. 
"""
db = create_conn()
def concat_name(database):
    
    concat_names = database.run("""ALTER TABLE customers
                                DROP COLUMN first_name;
                                ALTER TABLE customers
                                DROP COLUMN last_name;
                                SELECT * 
                                FROM customers 
                                LIMIT 10;""")
    return concat_names

print(concat_name(db))

