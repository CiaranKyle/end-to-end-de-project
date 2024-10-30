from names import get_first_name, get_last_name
import json
import random
from faker import Faker

fake = Faker()
products = ['Hat', 'Scarf', 'Hoodie', 'tshirt', 'Watch', 'Trousers', 'Accessory', 'Jewellery']
cities = ['Liverpool', 'Manchester', 'London', 'Sheffield', 'Leeds', 'York', 'Birmingham']
data = []

def customer_data_creation(num):
    """
    This function takes an integer as an input and creates a JSON file
    with that number of entries. This JSON file will be used as our 
    raw dataset for parsing further down the line. Inside the function
    we have a for loop and we are making use of the names module to
    generate random first names. Each customer is given a random age,
    random sample of products that they 'bought', and a random satisfaction
    rating. 

    Maybe consider adding shopping preferences.
    """
    for _ in range(num):

        people = {
            'first_name': get_first_name(),
            'last_name': get_last_name(),
            'age': random.randint(18, 65),
            'items_bought': random.sample(products, k=random.randint(0, len(products)-1)),
            'satisfaction_rating': random.choice(random.choices(
            [1, 2, 3, 4, 5], weights=[0.05, 0.15, 0.2, 0.4, 0.2])),
            'city': random.choice(cities), 
            'date_of_purchase': str(fake.date_between(start_date='-2y', end_date='today'))
        }

        data.append(people)

    data_to_json = { 'data': data }
    json_obj = json.dumps(data_to_json, indent=2)

    with open("db/data/customer.json", 'w') as f:
        f.write(json_obj)

def product_data_creation():
    """
    This function is creating a raw JSON file with the products that
    the shop sells and when parsed in the next part of this project
    """
    products_data = []
    
    for product in products:
        product_data_dict = {
            'product_name': product,
            'price': round(random.uniform(30, 50))
        }
        
        products_data.append(product_data_dict)

    product_to_json = { 'products': products_data}
    json_products = json.dumps(product_to_json, indent=2)

    with open("db/data/product.json", 'w') as f:
        f.write(json_products)
    
customer_data_creation(10000)
product_data_creation()
