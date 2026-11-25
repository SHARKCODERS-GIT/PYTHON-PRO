# Aula 15 | Extra 1 | Contar elementos

import json

with open("dados.json", encoding="utf-8") as f:
    dados = json.load(f)

idades = [e["idade"] for e in dados.values()]
print("Funcionários:", len(dados))
print(f"Média de idades: {sum(idades) / len(idades):.1f}")
