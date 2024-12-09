from pg8000.native import Connection
import os
from dotenv import load_dotenv

load_dotenv()

user = os.environ['USER']

password = os.environ['PASSWORD']
database = os.environ['DATABASE']

def create_conn():

    conn = Connection(user, database=database, password=password)
    return conn

def close_db(conn):
    conn.close()
