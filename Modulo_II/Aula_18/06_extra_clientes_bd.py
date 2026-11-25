# Aula 18 | Extra 1 | Tabela de clientes

import sqlite3

c = sqlite3.connect("loja.db")
c.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT UNIQUE, cidade TEXT)")
c.executemany("INSERT INTO clientes (nome, email, cidade) VALUES (?, ?, ?)", [("Ana Silva", "ana@email.pt", "Braga"), ("Rui Costa", "rui@email.pt", "Porto")])
c.commit()
print(c.execute("SELECT COUNT(*) FROM clientes").fetchone()[0], "clientes")
c.close()
