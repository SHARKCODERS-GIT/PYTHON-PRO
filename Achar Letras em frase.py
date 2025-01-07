def acharletra():
    soma = 0
    nome = input('Qual o frase? ')
    letra = input('Qual letras deseja procurar? ')
    for x in nome:
        if x == letra:
            soma += 1
    print(f'Esta frase tem {soma} letras {letra}')

acharletra()