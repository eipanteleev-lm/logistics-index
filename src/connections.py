import psycopg2
import pandas as pd
import config

def operations_weekly(item, store):
    query = open('queries/operations_weekly.sql').read()
    query = query.format(product_code=item, store_id=store)
    with psycopg2.connect(**config.CONNECTION_PARAMETERS) as conn:
        df = pd.read_sql(query, conn)

    return df

def operations(item, store):
    query = open('queries/operations.sql').read()
    query = query.format(product_code=item, store_id=store)
    with psycopg2.connect(**config.CONNECTION_PARAMETERS) as conn:
        df = pd.read_sql(query, conn)

    return df

def price(item, store):
    query = open('queries/price.sql').read()
    query = query.format(product_code=item, store_id=store)
    with psycopg2.connect(**config.CONNECTION_PARAMETERS) as conn:
        cur = conn.cursor()
        r = cur.execute(query).fetchone()

    return r
