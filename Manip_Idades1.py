def cadastro():
    nome = input('Entre com o nome: ')
    idade = int(input('Entre com a idade: '))
    with open('Lista_Idades.txt','a') as file:
        file.write(nome + '\n')
        file.write(str(idade) + '\n')