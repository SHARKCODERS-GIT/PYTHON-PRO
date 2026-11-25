# Aula 07 | Desafio | Quiz com jackpot

from random import sample

perguntas = [
    ["Capital de Portugal?", "lisboa"],
    ["Quanto é 7 x 8?", "56"],
    ["Maior planeta do sistema solar?", "júpiter"],
    ["Rio que passa no Porto?", "douro"],
    ["Quantos lados tem um hexágono?", "6"],
    ["Linguagem deste curso?", "python"]
]

jackpot = 0
for pergunta, resposta in sample(perguntas, 4):
    r = input(pergunta + " ").strip().lower()
    if r == resposta:
        jackpot = jackpot + 2500
        print(f"Certo! Jackpot: {jackpot} €")
    else:
        jackpot = 0
        print("Errado! Perdeu tudo.")
        break

if jackpot == 10000:
    print("Parabéns! Ganhou o prémio máximo de 10 000 €!")
