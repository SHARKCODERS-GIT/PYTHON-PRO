# Aula 13 | Exercício 1 | Procurar uma palavra

def procurar(nome, palavra):
    with open(nome, "r", encoding="utf-8") as f:
        for n, linha in enumerate(f, 1):
            if palavra.lower() in linha.lower():
                print(f"{n}: {linha.strip()}")

procurar("frases.txt", input("Palavra a procurar? "))
