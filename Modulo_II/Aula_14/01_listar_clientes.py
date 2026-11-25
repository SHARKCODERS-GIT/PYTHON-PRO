# Aula 14 | Exercício 1 | Listar clientes

import csv

with open("clientes.csv", "r", encoding="utf-8") as f:
    print(f"{'Nome':<14}{'Cidade':<10}{'Compras':>8}")
    for c in csv.DictReader(f):
        print(f"{c['nome']:<14}{c['cidade']:<10}{c['compras']:>8}")
