def cadastro():
    nome = input('Entre com o nome: ')
    idade = int(input('Entre com a idade: '))
    with open('Lista_Idades.txt','a') as file:
        file.write(nome + '\n')
        file.write(str(idade) + '\n')

def buscar():
    nome = input('Entre com o nome para busca: ')
    with open('Lista_Idades.txt','r') as file:
        for linha in file:
            if nome in linha:
                print('Idade:' + file.readline())

print('-='*12)
print('Manipulação de Arquivos')
print('-='*12)
print()
while True:
    print('0 - Sair\n1 - Cadastrar\n2 - Buscar')
    opc = int(input('Opção desejada: '))
    if opc == 0:
        print()
        print('Obrigado por utilizar o programa')
        break
    elif opc == 1:
        print()
        cadastro()
    elif opc == 2:
        print()
        buscar()
    else:
        print('Opção Inválida')