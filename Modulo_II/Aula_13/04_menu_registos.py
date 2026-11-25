# Aula 13 | Exercício 4 | Menu de registos

def registar():
    nome = input("Nome? ").strip().title()
    idade = int(input("Idade? "))
    with open("idades.txt", "a", encoding="utf-8") as f:
        f.write(f"{nome};{idade}\n")

while True:
    op = input("1 Registar | 0 Sair? ")
    if op == "1":
        registar()
    elif op == "0":
        print("Obrigado por utilizar o programa.")
        break
    else:
        print("Opção inválida.")
