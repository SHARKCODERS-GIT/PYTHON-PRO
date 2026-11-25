# Aula 18 | Exercício 4 | Inserir vários de uma vez

import sqlite3

novos = [
    ("Tablet Samsung", "10 polegadas, 64 GB", 229.90, 9),
    ("Auriculares Sony", "Bluetooth, cancelamento de ruído", 99.90, 20),
    ("Disco SSD 1 TB", "NVMe", 79.90, 15),
]
conexao = sqlite3.connect("loja.db")
conexao.executemany("INSERT INTO produtos (produto, descricao, preco, stock) VALUES (?, ?, ?, ?)", novos)
conexao.commit()
total = conexao.execute("SELECT COUNT(*) FROM produtos").fetchone()[0]
print("Produtos na base de dados:", total)
conexao.close()
