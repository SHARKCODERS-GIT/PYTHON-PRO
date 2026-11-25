# Aula 13 | Exercício 5 | Procurar uma pessoa

def procurar(nome):
    with open("idades.txt", "r", encoding="utf-8") as f:
        for linha in f:
            n, idade = linha.strip().split(";")
            if n.lower() == nome.lower():
                return f"Nome: {n} · Idade: {idade} anos"
    return "Não encontrado."

while True:
    op = input("2 Procurar | 0 Sair? ")
    if op == "2":
        print(procurar(input("Nome? ").strip()))
    elif op == "0":
        print("Obrigado por utilizar o programa.")
        break
