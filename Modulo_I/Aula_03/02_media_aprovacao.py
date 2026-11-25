# Aula 03 | Exercício 2 | Média e aprovação

nome = input("Nome do aluno? ")
n1 = float(input("Nota 1? "))
n2 = float(input("Nota 2? "))

media = (n1 + n2) / 2
print(nome, "teve média", media)

if media >= 9.5:
    print("Parabéns! Foi aprovado(a).")
else:
    print("Infelizmente, foi reprovado(a).")
