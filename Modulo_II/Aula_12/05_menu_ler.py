# Aula 12 | Exercício 5 | Ler todo o conteúdo

def ler_ficheiro(nome):
    try:
        with open(nome, "r", encoding="utf-8") as f:
            for i, linha in enumerate(f.readlines(), 1):
                print(f"{i}. {linha.strip()}")
    except FileNotFoundError:
        print("O ficheiro não existe.")

while True:
    op = input("3 Ler | 0 Sair? ")
    if op == "0":
        break
    if op == "3":
        ler_ficheiro(input("Ficheiro? ").strip())
