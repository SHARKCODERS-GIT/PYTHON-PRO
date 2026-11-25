# Aula 18 | Desafio | Loja com categorias

import sqlite3

c = sqlite3.connect("loja_completa.db")
c.executescript("""
CREATE TABLE IF NOT EXISTS categorias (id INTEGER PRIMARY KEY, nome TEXT NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS artigos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, preco REAL NOT NULL,
    categoria_id INTEGER REFERENCES categorias(id));
""")
c.executemany("INSERT OR IGNORE INTO categorias VALUES (?, ?)", [(1, "Informática"), (2, "Televisores"), (3, "Eletrodomésticos")])
c.executemany("INSERT INTO artigos (nome, preco, categoria_id) VALUES (?, ?, ?)",
              [("Portátil", 649.9, 1), ("Rato", 19.9, 1), ("Smart TV 48\"", 699.9, 2), ("Frigorífico", 549.0, 3), ("Micro-ondas", 129.0, 3)])
c.commit()
for nome, preco, cat in c.execute("SELECT a.nome, a.preco, c.nome FROM artigos a JOIN categorias c ON a.categoria_id = c.id"):
    print(f"{nome:<14}{preco:>8.2f} €  {cat}")
c.close()
