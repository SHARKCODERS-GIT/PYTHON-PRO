# Aula 04 | Desafio | Combate de boxe automático

from random import randint

vida_a = 100
vida_b = 100
ronda = 0

while vida_a > 0 and vida_b > 0:
    ronda = ronda + 1
    vida_b = vida_b - randint(5, 25)
    vida_a = vida_a - randint(5, 25)
    print("Ronda", ronda, "· Lutador A:", max(vida_a, 0), "· Lutador B:", max(vida_b, 0))

if vida_a > vida_b:
    print("Vence o Lutador A em", ronda, "rondas!")
elif vida_b > vida_a:
    print("Vence o Lutador B em", ronda, "rondas!")
else:
    print("Empate!")
