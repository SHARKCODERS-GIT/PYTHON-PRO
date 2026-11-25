# Aula 08 | Exercício 1 | Somar uma lista com for

numeros = [1, 2, 3, 4, 5, 6]
soma = 0

for n in numeros:
    soma = soma + n

print("Soma com for:", soma)
print("Soma com sum():", sum(numeros))
