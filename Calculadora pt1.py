import math

def escolher_funcao():
    global escolha
    print()
    print(' 0 - Sair              1 - Soma               2 - Subtrair')
    print(' 3 - Dividir           4 - Multiplicar        5 - Raiz Quadrada')
    print(' 6 - Potência          7 - Volume do Prisma   8 - Volume do Cilindro')
    print(' 9 - Volume Cone       10 - Volume Esfera')
    print()
    escolha = int(input('Qual sua escolha? '))
    print()

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


def raiz():
    r = math.sqrt(x)
    print('A raiz quadrada de',x,'é',round(r,2))


def potencia():
    r = x**y
    print('A potencia de',x,'elevado a',y,'é',round(r,2))


def v_prisma():
    r = x*y*z
    print('O volume deste prisma é de',round(r,2),'m3')


def v_cilindro():
    r = math.pi*(x**2)*y
    print('O volume deste cilindro é de',round(r,2),'m3')


def v_cone():
    r = (math.pi*(x**2)*y)/3
    print('O volume deste cone é de',round(r,2),'m3')


def v_esfera():
    r = (4*math.pi*(x**3))/3
    print('O volume desta esfera é de',round(r,2),'m3')


while True:
    escolher_funcao()
    if escolha==0:
        break
    elif escolha in [1,4]:
        x = int(input('Entre com o valor A: '))
        y = int(input('Entre com o valor B: '))
        if escolha==1:
            soma()
        elif escolha==2:
            sub()
        elif escolha==3:
            div()
        elif escolha==4:
            mult()
    elif escolha==5:
        x = int(input('Entre com os valor para Raiz Quadrada: '))
        raiz()
    elif escolha==6:
        x = int(input('Entre com os valor A: '))
        y = int(input('Qual potência?: '))
        potencia()
    elif escolha==7:
        x = int(input('Entre com a Largura: '))
        y = int(input('Entre com o Comprimento: '))
        z = int(input('Entre com a Altura: '))
        v_prisma()
    elif escolha in [8, 9]:
        x = int(input('Entre com o Raio: '))
        y = int(input('Entre com a Altura: '))
        if escolha==8:
            v_cilindro()
        elif escolha==9:
            v_cone()
    if escolha==10:
        x = int(input('Entre com o Raio: '))
        v_esfera()