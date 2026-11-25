# Aula 13 | Desafio | Estatísticas de idades

pessoas = {}
with open("idades.txt", "r", encoding="utf-8") as f:
    for linha in f:
        if linha.strip():
            nome, idade = linha.strip().split(";")
            pessoas[nome] = int(idade)

print("Pessoas:", len(pessoas))
print(f"Média: {sum(pessoas.values()) / len(pessoas):.1f} anos")
print("Mais velha:", max(pessoas, key=pessoas.get))
print("Mais nova:", min(pessoas, key=pessoas.get))
