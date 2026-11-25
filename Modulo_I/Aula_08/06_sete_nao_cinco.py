# Aula 08 | Exercício 6 | Divisíveis por 7, não múltiplos de 5

resultado = [n for n in range(101)
             if n % 7 == 0 and n % 5 != 0]

print(resultado)
