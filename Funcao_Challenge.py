from random import randint

lista = []

def sorteio():
    for x in range(10):
        y = randint(1,20)
        lista.append(y)
    print(f'Os valores sorteados foram {lista}')

def soma():
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f'A soma dos valores pares contidos na lista {lista} é {soma}')

sorteio()
soma()