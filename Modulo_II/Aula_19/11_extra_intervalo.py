# Aula 19 | Extra 5 | Pesquisa por intervalo de preço

import sqlite3

minimo = float(input("Preço mínimo? "))
maximo = float(input("Preço máximo? "))
c = sqlite3.connect("loja.db")
for p, preco in c.execute("SELECT produto, preco FROM produtos WHERE preco BETWEEN ? AND ?", (minimo, maximo)):
    print(f"{p}: {preco:.2f} €")
c.close()
