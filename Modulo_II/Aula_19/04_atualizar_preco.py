# Aula 19 | Exercício 4 | Atualizar o preço

import sqlite3

c = sqlite3.connect("loja.db")
produto = input("Produto a atualizar? ").strip()
novo = float(input("Novo preço? "))

cur = c.execute("UPDATE produtos SET preco = ? WHERE produto = ?", (novo, produto))
c.commit()
if cur.rowcount == 0:
    print("Produto não encontrado.")
else:
    print("Atualizado:", c.execute("SELECT produto, preco FROM produtos WHERE produto = ?", (produto,)).fetchone())
c.close()
