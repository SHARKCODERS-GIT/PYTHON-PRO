# Aula 14 | Exercício 5 | Exportar um filtro

import csv

with open("clientes.csv", "r", encoding="utf-8") as f:
    clientes = list(csv.DictReader(f))

vip = [c for c in clientes if int(c["compras"]) >= 5]
with open("clientes_vip.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=clientes[0].keys())
    escritor.writeheader()
    escritor.writerows(vip)
print(len(vip), "clientes VIP exportados.")
