# Aula 14 | Extra 4 | CSV para Excel português

import csv

with open("clientes.csv", encoding="utf-8") as f:
    linhas = list(csv.reader(f))

with open("clientes_pt.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter=";").writerows(linhas)

print(open("clientes_pt.csv", encoding="utf-8").readline().strip())
