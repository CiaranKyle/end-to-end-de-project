from db.connection import create_conn, close_db
import csv

"""Need to Unnest the data in the customers table. Split out the products and 
orders placed. Then we can make a column in customers table of how much a 
customer has spent to date. 
"""

def initial_extraction():
    """This function is a simple query by selecting all columns from a given database.
    The default variables are: db, customers and 10."""


    db = create_conn()
    select_query = db.run(
        """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name != '_prisma_migrations'"""
        )
    extracted_tables = []
    """Query each table to extract all information it contains"""
    for table in select_query:

        file_name = f'{[table[0]]}'
        rows = db.run(f"SELECT * FROM {table[0]}")
        columns = [col["name"] for col in db.columns]

        if rows:
            with open(f"{table[0]}.csv", 'w') as file:
                writer = csv.writer(file)
                writer.writerow(columns)
                writer.writerows(rows)
            extracted_tables.append(table[0])

    close_db(db)

    return extracted_tables

initial_extraction()
    
