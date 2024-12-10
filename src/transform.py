import pandas as pd
from src.extract import initial_extraction
from src.transform_util_functions import customers, orders, products

def transform():
    """This function takes no arguments, but in a data pipeline it would take an event.
    It has no orchestration due to being ran on my local environment and no cloud services.
    So, the transform function itself calls the initial_extraction function from the extract.py
    file. This gives a list of csv file names we can now transform into OLAP format.
    There is a function dictionary so we can assign a function to the table given.
    """

    function_dictionary = {
        'db/data/products.csv' : products,
        'db/data/orders.csv' : orders,
        'db/data/customers.csv' : customers
    }

    files = initial_extraction()

    for file in files:
        df = pd.read_csv(file)
        updated_df = function_dictionary[file](df)
        print(updated_df)

    return []

transform()
        