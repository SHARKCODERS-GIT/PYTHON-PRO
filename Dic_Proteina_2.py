proteina = {'Soja':56,'Camarão':24,'Frango':23,'Peixes':20,'Leite':8}

def alfa():
    for x in sorted(proteina.items()):
        print(f'{x[0]} : {x[1]} de proteína a cada 100g')

def grau():
    for x in sorted(proteina, key=proteina.get, reverse=True):
        print(f'{proteina[x]} de proteína a cada 100g no {x}')

print('-='*10)
print('Lista de Proteínas')
print('-='*10)
print('1 - Ordem Alfabética\n2 - Ordem Proteica')
opc = int(input('Opção desejada: '))
if opc == 1:
    print()
    alfa()
elif opc == 2:
    print()
    grau()
else:
    print('Opção Inválida')