import psycopg2 as psy
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
QUERIE = os.getenv('QUERIE')

def exec(host, database, user, password):
    with psy.connect(host=host, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            with open('src/queries/source.sql', 'r') as querie:
                script = querie.read()
                cur.execute(script)
                result = cur.fetchall()
                print(result)

if __name__ == "__main__":
    exec(host=HOST, database=DATABASE, user=USER, password=PASSWORD)

