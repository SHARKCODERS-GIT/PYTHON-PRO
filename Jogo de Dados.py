import random

def jogo_dados():
    jogadores = {}
    num_jogadores = int(input("Quantos jogadores participarão? "))
    
    for i in range(1, num_jogadores + 1):
        nome = input(f"Digite o nome do jogador {i}: ")
        jogadores[nome] = random.randint(1, 20)
    
    print("\nResultados:")
    for jogador, resultado in jogadores.items():
        print(f"{jogador}: {resultado}")
    
    vencedor = max(jogadores, key=jogadores.get)
    print(f"\nO vencedor é {vencedor} com {jogadores[vencedor]} pontos!")

jogo_dados()

