# Aula 11 | Desafio | Classificação de um jogo de dados

from random import randint

def registar_jogadores():
    jogadores = {}
    n = int(input("Quantos jogadores? "))
    for i in range(1, n + 1):
        nome = input(f"Nome do jogador {i}? ").strip().title()
        jogadores[nome] = randint(1, 20)
    return jogadores

def classificacao(jogadores):
    ordem = sorted(jogadores, key=jogadores.get, reverse=True)
    for pos, nome in enumerate(ordem, 1):
        print(f"{pos}.º {nome:<8} {jogadores[nome]:>2} pontos")
    print(f"Vencedor: {ordem[0]}!")

classificacao(registar_jogadores())
