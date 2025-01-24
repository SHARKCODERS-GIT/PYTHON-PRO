def cadastro():
    nome = input('Entre com o nome: ')
    idade = int(input('Entre com a idade: '))
    with open('Lista_Idades.txt','a') as file:
        file.write(nome + '\n')
        file.write(str(idade) + '\n')

print('-='*12)
print('Manipulação de Arquivos')
print('-='*12)
print()
while True:
    print('0 - Sair\n1 - Cadastrar')
    opc = int(input('Opção desejada: '))
    if opc == 0:
        print()
        print('Obrigado por utilizar o programa')
        break
    if opc == 1:
        print()
        cadastro()
    else:
        print('Opção Inválida')