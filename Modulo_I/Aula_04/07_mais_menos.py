# Aula 04 | Exercício 7 | Jogo do mais ou menos

from random import randint

secreto = randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Palpite? "))
    tentativas = tentativas + 1
    if palpite == secreto:
        print("Acertou em", tentativas, "tentativas!")
        break
    elif palpite < secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")
