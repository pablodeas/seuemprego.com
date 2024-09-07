import psycopg2 as psy

with psy.connect("dbname=seuemprego user=pablodeas") as conn:
    with conn.cursor() as cur:
        pass