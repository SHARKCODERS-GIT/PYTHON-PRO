# Aula 18 | Extra 4 | Valor do stock

import sqlite3

c = sqlite3.connect("loja.db")
total = c.execute("SELECT SUM(preco * stock) FROM produtos").fetchone()[0]
print(f"Valor total do stock: {total:,.2f} €".replace(",", " "))
c.close()
