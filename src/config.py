import os

POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'postgres')
POSTGRES_PORT = int(os.getenv('POSTGRES_PORT', 5432))
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

CONNECTION_PARAMETERS = {
    'host': POSTGRES_HOST,
    'port': POSTGRES_PORT,
    'dbname': POSTGRES_DB,
    'user': POSTGRES_USER,
    'password': POSTGRES_PASSWORD
}