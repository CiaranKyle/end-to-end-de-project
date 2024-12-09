from db.connection import create_conn, close_db
import csv

"""Need to Unnest the data in the customers table. Split out the products and 
orders placed. Then we can make a column in customers table of how much a 
customer has spent to date. 
"""

def initial_extraction():
    """This function takes all the tables from the database puts the tables into
    csv files. By connecting to the database and selecting all tables from the schema
    then selecting all the columns from these tables separately."""


    db = create_conn()
    select_query = db.run(
        """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name != '_prisma_migrations'"""
        )
    extracted_tables = []
    """Query each table to extract all information it contains"""
    for table in select_query:

        file_name = f'db/data/{table[0]}.csv'
        rows = db.run(f"SELECT * FROM {table[0]}")
        columns = [col["name"] for col in db.columns]

        if rows:
            with open(file_name, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(columns)
                writer.writerows(rows)
            extracted_tables.append(file_name)

    close_db(db)

    return extracted_tables