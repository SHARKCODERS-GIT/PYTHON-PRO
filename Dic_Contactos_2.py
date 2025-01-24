contatos = {'Roberto':'988 777 666','João':'977 666 555','Mario':'999 888 777'}

def buscar():
    nome = input('Quem deseja procurar: ')
    print(f'Número: {contatos[nome]}')

def cadastro():
    nome = input('Quem deseja cadastrar: ')
    tel = input('Numero do telefone: ')
    contatos[nome] = tel
    print(f'Nova agenda contem {len(contatos)} contatos')

def apagar():
    nome = input('Quem deseja apagar dos registros: ')
    contatos.pop(nome)
    print(f'Nova agenda contem {len(contatos)} contatos')

print('-='*10)
print('Cadastro Telefonico')
print('-='*10)
print()
while True:
    print('0 - Sair\n1 - Buscar\n2 - Cadastrar\n3 - Apagar')
    opc = int(input('Opção desejada: '))
    if opc == 0:
        print()
        print('Obrigado por utilizar o programa')
        break
    elif opc == 1:
        print()
        buscar()
        print()
    elif opc == 2:
        print()
        cadastro()
        print()
    elif opc == 3:
        print()
        apagar()
        print()
    else:
        print('Opção Inválida')