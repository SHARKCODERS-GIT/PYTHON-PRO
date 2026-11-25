# Aula 12 | Exercício 4 | Menu para inserir frases

def criar_ficheiro(nome):
    with open(nome, "w", encoding="utf-8") as f:
        pass
    print(f"Ficheiro {nome} criado.")

def inserir_frase(nome, frase):
    with open(nome, "a", encoding="utf-8") as f:
        f.write(frase + "\n")
    print("Frase inserida.")

while True:
    op = input("1 Criar | 2 Inserir frase | 0 Sair? ")
    if op == "0":
        break
    nome = input("Ficheiro? ").strip()
    if op == "1":
        criar_ficheiro(nome)
    elif op == "2":
        inserir_frase(nome, input("Frase? "))
