import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        password TEXT NOT NULL,
        
);
""")

