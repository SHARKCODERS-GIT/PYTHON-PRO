# Aula 04 | Exercício 6 | Lançar dados até sair duplo 6

from random import randint

lancamentos = 0

while True:
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    lancamentos = lancamentos + 1
    print("Lançamento", lancamentos, ":", d1, "e", d2)
    if d1 == 6 and d2 == 6:
        break

print("Foram precisos", lancamentos, "lançamentos.")
