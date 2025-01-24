import csv

with open('Haiti_CSV.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        if 'HI' in linha:
            print('Nome:', linha[0], linha[1], '\nNumero:', linha[2],linha[3],
                  '\nUltima Coordenada: LAT:', linha[9],'LON:', linha[10],'\n')