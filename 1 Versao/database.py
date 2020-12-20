import sqlite3

conn = sqlite3.connect('usuarios.db')

cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        User TEXT NOT NULL,
        Password TEXT NOT NULL
        
);
""")

print ("Banco criado com sucesso.")


