import sqlite3

conn = sqlite3.connect('usuarios.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE usuarios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        password TEXT NOT NULL,
        
);
""")

