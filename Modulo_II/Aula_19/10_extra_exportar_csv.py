# Aula 19 | Extra 4 | Exportar para CSV

import csv, sqlite3

c = sqlite3.connect("loja.db")
linhas = c.execute("SELECT id, produto, descricao, preco, stock FROM produtos").fetchall()
c.close()

with open("produtos.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "produto", "descricao", "preco", "stock"])
    w.writerows(linhas)
print(len(linhas), "produtos exportados.")
