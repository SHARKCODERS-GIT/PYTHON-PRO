filmes = {'Roberto':'988 777 666','João':'977 666 555','Mario':'999 888 777'}

def buscar():
    nome = input('Quem deseja procurar: ')
    print(f'Número: {filmes[nome]}')

buscar()