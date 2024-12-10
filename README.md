
This project starts off by creating randomly generated data and storing this into a JSON file. This is trying to replicate customer data and the products that
they buy from a clothing store maybe.

To run this you will need to set up your own .env file so that you can have
the psql username and password as well as the de-project database information held securely. Once the database is seeded and two tables, customer and product, have been created I will make a separate Python file 
which will handle the data normalisation of the tables in the database. 
This will split out into 4 tables. Customer info (I may go back and add 
more random data to customer.json creation), Order, OrderItem and, Product. These will link together and queries can be made from these tables.  

The random data includes, a data of purchase, the city the customer was in, age, first and last names, items bought, satisfaction rating and the date of purchase.

The project will be built on skills I have learned from the data engineering bootcamp course at Northcoders. As I'm just over halfway through this it won't be a
completed and glossy project. I will use API to call to the OLAP database towards the backend of this project.
