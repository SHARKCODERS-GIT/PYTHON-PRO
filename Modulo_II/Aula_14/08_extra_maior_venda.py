# Aula 14 | Extra 2 | Maior venda

import csv

with open("vendas.csv", encoding="utf-8") as f:
    vendas = list(csv.DictReader(f))

maior = max(vendas, key=lambda v: int(v["quantidade"]) * float(v["preco"]))
total = int(maior["quantidade"]) * float(maior["preco"])
print(f"{maior['data']} · {maior['produto']} · {total:.2f} €")
