# Aula 19 | Extra 1 | Ordenar por preço

import sqlite3

c = sqlite3.connect("loja.db")
for p, preco in c.execute("SELECT produto, preco FROM produtos ORDER BY preco DESC"):
    print(f"{p:<22}{preco:>8.2f} €")
c.close()
