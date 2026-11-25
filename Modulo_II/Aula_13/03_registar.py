# Aula 13 | Exercício 3 | Registar pessoas

def registar():
    nome = input("Nome? ").strip().title()
    idade = int(input("Idade? "))
    with open("idades.txt", "a", encoding="utf-8") as f:
        f.write(f"{nome};{idade}\n")
    print(f"{nome} registado(a).")

registar()
