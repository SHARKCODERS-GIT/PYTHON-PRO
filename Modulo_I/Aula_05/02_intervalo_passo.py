# Aula 05 | Exercício 2 | Intervalo com passo

inicio = int(input("Início? "))
fim = int(input("Fim? "))
passo = int(input("Passo? "))

for i in range(inicio, fim + 1, passo):
    print(i, end=" ")
