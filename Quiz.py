from random import randint

soma = 0

p1 = 'Qual o feminino de Leão? '
p2 = 'Qual o feminino de Elefante? '
p3 = 'Qual o feminino de João? '
p4 = 'Qual o feminino de Gato? '

pergunta = [p1,p2,p3,p4]
resposta = ['Leoa','Elefanta','Joana','Gata']
lista = []

while True:
    x = randint(0, 3)

    if soma == 1000:
        print('Parabens! Ficou milionário')
        break

    if x not in lista:
        lista.append(x)

        y = input(pergunta[x])
        z = resposta[x]
        if y.title() == z:
            soma += 250
            print('Certa resposta')
            print(f'Ganhou 250 mil euros. Está com {soma} mil euros')
            print()
        else:
            print('Perdeu tudo!')
            break