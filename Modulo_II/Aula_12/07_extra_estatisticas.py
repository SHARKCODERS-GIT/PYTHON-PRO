# Aula 12 | Extra 1 | Contar palavras de um ficheiro

with open("3_linhas.txt", "r", encoding="utf-8") as f:
    texto = f.read()

print("Linhas:", len(texto.splitlines()))
print("Palavras:", len(texto.split()))
print("Caracteres:", len(texto))
