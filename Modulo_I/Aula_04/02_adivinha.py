# Aula 04 | Exercício 2 | Adivinha o número

from random import randint

secreto = randint(0, 5)
palpite = int(input("Em que número de 0 a 5 pensei? "))

print("Eu escolhi o número", secreto)
if palpite == secreto:
    print("Parabéns! Acertou.")
else:
    print("Errou! Tente novamente.")
