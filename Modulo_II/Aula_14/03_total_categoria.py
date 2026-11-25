# Aula 14 | Exercício 3 | Total por categoria

import csv

totais = {}
with open("vendas.csv", "r", encoding="utf-8") as f:
    for v in csv.DictReader(f):
        valor = int(v["quantidade"]) * float(v["preco"])
        totais[v["categoria"]] = totais.get(v["categoria"], 0) + valor

for cat, total in totais.items():
    print(f"{cat:<12}{total:>9.2f} €")
print(f"{'Total':<12}{sum(totais.values()):>9.2f} €")
