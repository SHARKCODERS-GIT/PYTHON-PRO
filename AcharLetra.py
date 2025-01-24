def acharletra():
    nome = input('Digite a palavra? ')
    letra = input('Qual a letra? ')
    if letra in nome:
        print(f'Esta palavra tem a letra {letra}')
    else:
        print(f'Esta palavra não tem a letra {letra}')

acharletra()
