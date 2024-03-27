import sqlite3

conn = sqlite3.connect('bauru_participa.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS enquetes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS opcoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        enquete_id INTEGER NOT NULL,
        descricao TEXT NOT NULL,
        votos INTEGER DEFAULT 0,
        FOREIGN KEY (enquete_id) REFERENCES enquetes (id)
    )
''')

conn.commit()
conn.close()
