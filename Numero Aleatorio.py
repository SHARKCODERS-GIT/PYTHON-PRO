from random import randint

pc=randint(0,5) #varialvel de randomizar
user=int(input('Qual numero entre 0 e 5 eu estou pensando? '))
print()

#condicional
if user==pc:
    print('Parabens voce acertou')
else:
    print('Voce errou!')