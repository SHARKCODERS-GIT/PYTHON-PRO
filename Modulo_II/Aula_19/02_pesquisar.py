# Aula 19 | Exercício 2 | Pesquisar por nome

import sqlite3

texto = input("Pesquisar produto? ").strip()
c = sqlite3.connect("loja.db")
res = c.execute("SELECT produto, preco, stock FROM produtos WHERE produto LIKE ?", (f"%{texto}%",)).fetchall()

for prod, preco, stock in res:
    print(f"{prod} · {preco:.2f} € · {stock} em stock")
print(len(res), "resultado(s).")
c.close()
