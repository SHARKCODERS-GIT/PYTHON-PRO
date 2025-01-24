def total():
    with open('frases.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())

def procurar():
    texto = input('Qual a palavra que procuras? ')
    with open('frases.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            if texto in linha:
                print(linha.rstrip())

def contar():
    soma = 0
    with open('frases.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            soma += 1
    print(f'Numero de linhas no arquivo: {soma}')