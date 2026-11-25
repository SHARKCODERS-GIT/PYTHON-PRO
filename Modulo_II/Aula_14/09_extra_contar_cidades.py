# Aula 14 | Extra 3 | Clientes por cidade

import csv

cidades = {}
with open("clientes.csv", encoding="utf-8") as f:
    for c in csv.DictReader(f):
        cidades[c["cidade"]] = cidades.get(c["cidade"], 0) + 1

for cidade, n in sorted(cidades.items()):
    print(cidade, n)
