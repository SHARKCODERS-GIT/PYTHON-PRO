a= int(input('Entre com o primeiro numero: '))
b= int(input('Entre com o segundo numero: '))

for x in range (a,b+1):
    if x % 2 == 0:
        print(x, end=' ')

print()
print('FIM')