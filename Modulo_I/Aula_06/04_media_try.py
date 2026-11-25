# Aula 06 | Exercício 4 | Média com validação

try:
    n1 = float(input("Nota 1? "))
    n2 = float(input("Nota 2? "))
    n3 = float(input("Nota 3? "))
    media = (n1 + n2 + n3) / 3
    print(f"Média: {media:.1f}")
    if media >= 9.5:
        print("Aprovado(a)!")
    else:
        print("Reprovado(a).")
except ValueError:
    print("Erro: escreva apenas números.")
