# Aula 05 | Exercício 5 | Contar uma letra numa frase

frase = input("Escreva uma frase? ")
letra = input("Que letra quer contar? ")
contador = 0

for c in frase:
    if c == letra:
        contador = contador + 1

print("A letra", letra, "aparece", contador, "vezes.")
