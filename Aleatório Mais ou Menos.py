from random import randint

python = randint(1,100)
erros = 0

print('Escolha um número entre 1 e 100')
print()

while True:
    erros +=1
    perg = int(input('Digite seu palpite: '))
    if python > perg:
        print('Errado! O número é maior')
    elif python < perg:
        print('Errado! O número é menor')
    else:
        break

print('Foram necessárias',erros,'jogadas')