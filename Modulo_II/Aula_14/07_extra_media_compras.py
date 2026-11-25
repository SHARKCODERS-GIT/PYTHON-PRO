# Aula 14 | Extra 1 | Média de compras

import csv

with open("clientes.csv", encoding="utf-8") as f:
    compras = [int(c["compras"]) for c in csv.DictReader(f)]

print(f"Média de compras: {sum(compras) / len(compras):.1f}")
