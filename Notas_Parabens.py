n1=int(input('Qual a nota 1 do aluno? '))
n2=int(input('Qual a nota 2 do aluno? '))
med= (n1+n2)/2
if med>60:
    print('Paranbens! Sua média é', med, 'e esta acima da média')
else:
    print('Que pena! Sua média é', med, 'e esta abaixo da média')