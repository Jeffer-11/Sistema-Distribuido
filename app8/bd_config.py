import psycopg2
import psycopg2.extras

def get_db_connection():
    conn = psycopg2.connect(
        dbname='flaskdb',        # Tu base de datos
        user='jefferson',        # Tu usuario
        password='Zoe23',        # Tu contraseña
        host='localhost',        # Host local
        port='5432'              # Puerto por defecto
    )
    return conn
