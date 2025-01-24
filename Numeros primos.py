a= int(input('Entre com o numero: '))
b=0
for x in range (1,a+1):
    if a % x == 0:
        b+=1
        print(x, end=' ')

if b>2:
    print()
    print('O número',a,'foi divisível',b,'vezes!')
    print(a, 'não é um número primo')
else:
    print()
    print('O número', a, 'foi divisível', b, 'vezes!')
    print(a, 'é um número primo')
