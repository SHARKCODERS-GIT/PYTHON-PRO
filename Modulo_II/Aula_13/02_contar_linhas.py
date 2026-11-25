# Aula 13 | Exercício 2 | Contar linhas

def contar_linhas(nome):
    total = 0
    with open(nome, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip():
                total += 1
    return total

print("frases.txt tem", contar_linhas("frases.txt"), "linhas.")
