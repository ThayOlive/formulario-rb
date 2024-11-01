from django.test import TestCase

# Create your tests here.
from django.db import connections
from django.db.utils import OperationalError

def check_database_connection():
    db_conn = connections['default']
    try:
        db_conn.cursor()
        print("Conexão com o banco de dados bem-sucedida!")
    except OperationalError:
        print("Falha ao conectar ao banco de dados!")

