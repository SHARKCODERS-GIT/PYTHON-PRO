a= int(input('Entre com o primeiro numero: '))
b= int(input('Entre com o segundo numero: '))
escolha = int(input('1 - Par \n2 - Impar \nEscolha a opção: '))
print()

if escolha == 1:
    print('Os números pares são:')
    print()
elif escolha == 2:
    print('Os números impares são:')
    print()

for x in range (a,b+1):
    if escolha == 1:
        if x % 2 == 0:
            print(x, end=' ')
    elif escolha == 2:
        if x % 2 == 1:
            print(x, end=' ')
    else:
        print('Opção inválida')
        break

print()
print('FIM')