# Aula 15 | Exercício 2 | Todos os funcionários

import json

with open("dados.json", encoding="utf-8") as f:
    dados = json.load(f)

for codigo, emp in dados.items():
    mensal = emp["salario"] / 14
    print(f"{codigo}: {emp['nome']:<6} {emp['cargo']:<14} {mensal:>8.2f} €/mês")
