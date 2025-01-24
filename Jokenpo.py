from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Estas são as opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha uma opção? '))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('-=' * 15)
print("O computador escolheu", itens[pc])
print("Você escolheu", itens[jogador])
print('-=' * 15)
if pc == 0: # PC jogou Pedra
    if jogador==0:
        print('Empate')
    elif jogador==1:
        print('Você ganhou')
    elif jogador==2:
        print('Você perdeu')
    else:
        print('Jagada Inválida! Jogue novamente')
elif pc==1: # PC jogou Papel
    if jogador==0:
        print('Você perdeu')
    elif jogador==1:
        print('Empate')
    elif jogador==2:
        print('Você Ganhou')
    else:
        print('Jagada Inválida! Jogue novamente')
elif pc==2: # PC jogou Tesoura
    if jogador==0:
        print('Você ganhou')
    elif jogador==1:
        print('Você perdeu')
    elif jogador==2:
        print('Empate')
    else:
        print('Jagada Inválida! Jogue novamente')