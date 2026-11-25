# Aula 15 | Exercício 3 | Acrescentar um funcionário

import json

with open("dados.json", encoding="utf-8") as f:
    dados = json.load(f)

novo = {
    "nome": input("Nome? ").strip().title(),
    "cargo": input("Cargo? ").strip().title(),
    "idade": int(input("Idade? ")),
    "salario": int(input("Salário anual? ")),
}
dados[f"emp{len(dados) + 1}"] = novo

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)
print("Funcionário gravado.")
