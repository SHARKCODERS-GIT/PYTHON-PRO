def soma():
    r = x+y
    print('O resultado da soma é',r)


def sub():
    r = x-y
    print('O resultado da subtração é', r)


def div():
    r = x/y
    print('O resultado da divisão é', r)


def mult():
    r = x*y
    print('O resultado da multiplicação é', r)


while True:
    print()
    print(' 0 - Sair\n 1 - Soma\n 2 - Subtrair\n 3 - Dividir\n 4 - Multiplicar\n 5 - Soma3n')
    print()
    escolha = int(input('Qual sua escolha? '))
    print()
    if escolha==0:
        break
    elif escolha!=0:
        x = int(input('Entre com os valor A: '))
        y = int(input('Entre com os valor B: '))
        if escolha==1:
            soma()
        elif escolha==2:
            sub()
        elif escolha==3:
            div()
        elif escolha==4:
            mult()