# Aula 18 | Exercício 1 | Base de dados da loja

import sqlite3

conexao = sqlite3.connect("minha_loja.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL UNIQUE,
    descricao TEXT NOT NULL,
    preco REAL NOT NULL,
    stock INTEGER NOT NULL
)""")
conexao.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tabelas:", cursor.fetchall())
conexao.close()
