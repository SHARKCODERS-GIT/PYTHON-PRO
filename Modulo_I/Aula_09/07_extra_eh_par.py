# Aula 09 | Extra 1 | Par ou ímpar

def eh_par(n):
    return n % 2 == 0

for numero in [4, 7, 10]:
    print(numero, "é par?", eh_par(numero))
