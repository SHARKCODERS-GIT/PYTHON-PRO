def criar():
    nome = input('Digite o nome do arquivo que deseja criar: ')
    with open(nome+'.txt', 'w', encoding='utf-8') as arquivo:
        print(f'Arquivo "{nome}.txt" criado com Sucesso')

def inserir():
    nome = input('Digite o nome do arquivo que deseja abrir: ')
    print(f'Arquivo "{nome}.txt" foi aberto com sucesso')
    print()
    frase = input('Digite a frase que deseja inserir: ')
    with open(nome+'.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(frase + '\n')
        print()
        print('Frase foi adicionada com sucesso')

def buscar():
    nome = input('Digite o nome do arquivo que deseja abrir: ')
    print(f'Arquivo "{nome}.txt" foi aberto com sucesso')
    print()
    with open(nome+'.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())

buscar()