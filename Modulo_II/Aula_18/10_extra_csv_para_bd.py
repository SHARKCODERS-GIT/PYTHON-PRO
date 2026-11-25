# Aula 18 | Extra 5 | Do CSV para a base de dados

import csv, sqlite3

with open("novos.csv", "w", encoding="utf-8") as f:
    f.write("produto,descricao,preco,stock\nColuna JBL,Bluetooth,59.90,11\nRouter TP-Link,Wi-Fi 6,89.90,5\n")

c = sqlite3.connect("loja.db")
with open("novos.csv", encoding="utf-8") as f:
    linhas = [(r["produto"], r["descricao"], float(r["preco"]), int(r["stock"])) for r in csv.DictReader(f)]
c.executemany("INSERT INTO produtos (produto, descricao, preco, stock) VALUES (?, ?, ?, ?)", linhas)
c.commit()
print(len(linhas), "produtos importados.")
c.close()
