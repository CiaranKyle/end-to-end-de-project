from db.seed import seed
from db.connection import create_conn, close_db
from db.data.data_creation import data_to_json, product_to_json
#need to import or read json files before they are passed to the seed.

# Do not change this code
db = None
try:
    db = create_conn()
    seed(db, data_to_json, product_to_json)
except Exception as e:
    print(e)
finally:
    if db:
        close_db(db)