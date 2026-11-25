# Aula 12 | Desafio | Diário de bordo

from datetime import date

def nova_entrada(texto):
    with open("diario.txt", "a", encoding="utf-8") as f:
        f.write(f"{date.today()} | {texto}\n")

def ver_diario():
    try:
        with open("diario.txt", "r", encoding="utf-8") as f:
            print(f.read().strip())
    except FileNotFoundError:
        print("O diário está vazio.")

while True:
    op = input("1 Nova entrada | 2 Ver diário | 0 Sair? ")
    if op == "1":
        nova_entrada(input("O que fez hoje? "))
    elif op == "2":
        ver_diario()
    elif op == "0":
        break
