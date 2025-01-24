from random import randint
from time import sleep

sorteio = {}

def cadastro():
    quant = int(input('Quantos jogadores terão? '))
    print()
    for x in range(1,quant+1):
        nome = input(f'Nome do jogador {x}º jogador: ')
        print('Numero sorteado atribuido com sucesso')
        print()
        num = randint(1,20)
        sorteio[nome] = num
    print('Processando ....')
    sleep(3)

def placar():
    y = 0
    for x in sorted(sorteio, key=sorteio.get, reverse=True):
        y += 1
        print(f'Em {y}º lugar com {sorteio[x]} pontos, ficou o jogador {x}')


cadastro()
placar()