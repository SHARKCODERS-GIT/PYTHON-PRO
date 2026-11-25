# Aula 07 | Exercício 2 | Pedra, papel ou tesoura

from random import choice

opcoes = ["pedra", "papel", "tesoura"]
jogador = input("Pedra, papel ou tesoura? ")
computador = choice(opcoes)
print("O computador escolheu", computador)

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Ganhou!")
else:
    print("Perdeu!")
