# Aula 14 | Exercício 2 | Clientes por cidade

import csv

cidade = input("Cidade? ").strip().title()
total = 0
with open("clientes.csv", "r", encoding="utf-8") as f:
    for c in csv.DictReader(f):
        if c["cidade"] == cidade:
            print(f"{c['nome']} · {c['telefone']}")
            total += 1
print(f"{total} cliente(s) em {cidade}.")
