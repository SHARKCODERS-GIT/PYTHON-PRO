# Aula 18 | Exercício 2 | Registar um produto

import sqlite3

produto = input("Produto? ").strip()
descricao = input("Descrição? ").strip()
preco = input("Preço? ").strip()
stock = input("Stock? ").strip()

if not all([produto, descricao, preco, stock]):
    print("Todos os campos são obrigatórios.")
else:
    conexao = sqlite3.connect("loja.db")
    conexao.execute("INSERT INTO produtos (produto, descricao, preco, stock) VALUES (?, ?, ?, ?)",
                    (produto, descricao, float(preco), int(stock)))
    conexao.commit()
    conexao.close()
    print(f"{produto} registado.")
