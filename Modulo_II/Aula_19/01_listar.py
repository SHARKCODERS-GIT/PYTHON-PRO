# Aula 19 | Exercício 1 | Listar produtos

import sqlite3

def listar():
    c = sqlite3.connect("loja.db")
    print(f"{'ID':<4}{'Produto':<22}{'Preço':>9}{'Stock':>7}")
    for id_, prod, preco, stock in c.execute("SELECT id, produto, preco, stock FROM produtos"):
        print(f"{id_:<4}{prod:<22}{preco:>9.2f}{stock:>7}")
    c.close()

listar()
