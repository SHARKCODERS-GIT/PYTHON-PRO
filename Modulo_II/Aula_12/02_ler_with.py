# Aula 12 | Exercício 2 | Ler com with

nome = input("Nome do ficheiro? ")

with open(nome, "r", encoding="utf-8") as f:
    texto = f.read()

print(texto)
print("Caracteres:", len(texto))
