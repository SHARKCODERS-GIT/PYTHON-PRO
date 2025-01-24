from random import randint
from time import sleep

print('Quantas jogadas serão necessárias até aparecer 2 dados de número 6?')
sleep(2)
num=0
DieOne = 0
DieTwo = 0

while True:
    num += 1
    DieOne = randint(1,6)
    DieTwo = randint(1,6)
    print(DieOne)
    print(DieTwo)
    sleep(0.2)
    print()
    if (DieOne == 6) and (DieTwo == 6):
        print('Os dois 6s apareceram depois de ', num, ' tentativas!')
        print()
        break