from random import randint
from time import sleep

vida_lee = 20
vida_mike = 30

print("Bem Vindos Sras e Srs a luta do século")
print("")
sleep(2)
print("Do meu lado esquerdo do corner")
print("Bruce Lee inicia a luta com", vida_lee, "de Vida")
sleep(4)
print("")
print("Do meu lado direito do corner")
print("Mike Ty inicia a luta com", vida_mike, "de Vida")
sleep(4)
print("")
print("Vamos iniciar a luta ...")
print("")
sleep(1)
print("FIGHT!")
print("")
sleep(1)

#condicional
while True:
    # aleatório para o soco
    soco_lee = randint(3, 8)
    soco_mike = randint(1, 5)

    # este é o código do Bruce Lee
    print('=-' * 17)
    print('Bruce Lee deu um soco de força', soco_lee)
    vida_mike -= soco_lee
    print('A vida do Mike Ty foi para', vida_mike)
    print('=-' * 17)
    sleep(4)
    print()
    if vida_mike < 1:
        print('Bruce Lee foi o vencedor desta luta!')
        break

    # este é o código do Mike Ty
    print('=-' * 17)
    print('Mike Ty deu um soco de força', soco_mike)
    vida_lee -= soco_mike
    print('A vida do Bruce Lee foi para', vida_lee)
    print('=-' * 17)
    sleep(4)
    print()
    if vida_lee < 1:
        print('Mike Ty foi o vencedor desta luta!')
        break

print("=-" * 20)
print("Obrigado por assistir mais esta emocionante luta!")