from db.seed import seed
from db.seed_analytics import seed_analytics
from db.connection import create_conn, close_db
import json
#need to import or read json files before they are passed to the seed.

with open("db/data/customer.json", 'r') as f:
    customers = json.load(f)

with open("db/data/product.json", 'r') as f:
    products = json.load(f)

db = None
try:
    db = create_conn()
    seed(db, customers, products)
    
except Exception as e:
    print(e)

finally:
    if db:
        close_db(db)