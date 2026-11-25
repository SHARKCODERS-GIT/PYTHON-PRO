# Aula 15 | Exercício 1 | Ficha de funcionária

import json

with open("dados.json", encoding="utf-8") as f:
    dados = json.load(f)

emp = dados["emp1"]
print("Funcionária:", emp["nome"])
print("Cargo:", emp["cargo"])
print("Idade:", emp["idade"], "anos")
print("Salário anual:", emp["salario"], "€")
