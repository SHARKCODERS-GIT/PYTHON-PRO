import csv

print('=-'*14)
print('Classics of Rock Repository')
print('=-'*14)

def busca():
    with open('classic_rock_playlist.csv', 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        print('1 - Artista ou Banda\n2 - Música\n3 - Ano de lançamento')
        opc = int(input('Opção: '))
        print()
        if opc == 1:
            nome = input('Digite pelo Artista ou Banda: ')
            for linha in leitor_csv:
                if nome.title() in linha:
                    print('Musica:',linha[1],'\nAlbum:',linha[2],'\nAno:',linha[3],'\nGenero:',linha[4])
                    print()
        elif opc == 2:
            nome = input('Digite pela Música: ')
            for linha in leitor_csv:
                if nome.title() in linha:
                    print('Artista:',linha[0],'\nAlbum:',linha[2],'\nAno:',linha[3],'\nGenero:',linha[4])
                    print()
        elif opc == 3:
            nome = input('Digite pelo Ano: ')
            for linha in leitor_csv:
                if nome.title() in linha:
                    print('\nMusica:',linha[1],'\nArtista:',linha[0],'\nAlbum:',linha[2],'\nGenero:',linha[4])
                    print()

def rating():
    with open('classic_rock_playlist.csv', 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        lista = list(leitor_csv)
        ano = input('Digite o Ano da pesquisa (2022 a 2015): ')
        if ano == '2022':
            lista_ordenada = sorted(lista, key = lambda ano: int(ano[5]))
            for linha in lista_ordenada:
                print('\nPosição:', linha[5], '\nMusica:', linha[1], '\nArtista:', linha[0])
                print()


while True:
    print('0 - Sair\n1 - Buscar\n2 - Ranking Anual')
    opc = int(input('Opção: '))
    print()
    if opc == 0:
        print('Obrigado por utilizar o programa')
        break
    elif opc == 1:
        busca()
    elif opc == 2:
        rating()