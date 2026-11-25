# Aula 08 | Exercício 4 | Converter para list comprehension

# Versão com for
lista = []
for item in range(1, 11):
    lista.append(item * 10)
print(lista)

# Versão com list comprehension
lista = [item * 10 for item in range(1, 11)]
print(lista)
