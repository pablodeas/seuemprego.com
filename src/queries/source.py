import psycopg2 as psy
import random
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

def exec_file(sql):
    with psy.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD) as conn:
        with conn.cursor() as cur:
            with open(sql, 'r') as querie:
                script = querie.read()
                cur.execute(script)
                return print(cur.fetchall())

def exec_normal(sql):
    with psy.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)

def new_pass():
    quanti = 8
    sequence = [str(random.randint(0, 9)) for _ in range(quanti)]
    password = ''.join(sequence)
    character = ['!', '@', '#', '$']
    pass_with_charac = password + random.choice(character)
    return pass_with_charac