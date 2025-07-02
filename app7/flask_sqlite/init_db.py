import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')

connection = sqlite3.connect(DB_PATH)

with open(SCHEMA_PATH) as f:
    connection.executescript(f.read())

cor = connection.cursor()

cor.execute('INSERT INTO posts (title,content) VALUES(?,?)',
('FIRST post', 'CONTENT FOR THE FIRST POST'))

cor.execute('INSERT INTO posts (title,content) VALUES(?,?)',
('SECOND post', 'CONTENT FOR THE SECOND POST'))

connection.commit()
connection.close()