# Aula 19 | Exercício 5 | Apagar com confirmação

import sqlite3

c = sqlite3.connect("loja.db")
produto = input("Produto a apagar? ").strip()
linha = c.execute("SELECT id, produto, preco FROM produtos WHERE produto = ?", (produto,)).fetchone()

if linha is None:
    print("Produto não encontrado.")
elif input(f"Apagar {linha}? (s/n) ").lower() == "s":
    c.execute("DELETE FROM produtos WHERE id = ?", (linha[0],))
    c.commit()
    print("Produto apagado. Restam", c.execute("SELECT COUNT(*) FROM produtos").fetchone()[0], "produtos.")
else:
    print("Operação cancelada.")
c.close()
