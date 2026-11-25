# Aula 15 | Extra 2 | Aumento salarial

import json

with open("dados.json", encoding="utf-8") as f:
    dados = json.load(f)

for emp in dados.values():
    emp["salario"] = round(emp["salario"] * 1.05)

with open("dados_atualizados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)
print({k: e["salario"] for k, e in dados.items()})
