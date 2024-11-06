from db.connection import create_conn, close_db

"""Need to Unnest the data in the customers table. Split out the products and 
orders placed. Then we can make a column in customers table of how much a 
customer has spent to date. 
"""
db = create_conn()
def select_10_entries(database):
    """This function is a simple query by selecting all columns from a given database.
    The default variables are: db, customers and 10."""

    select_query = database.run("""SELECT * FROM orders LIMIT 10;""")
    return select_query

    
print(select_10_entries(db))