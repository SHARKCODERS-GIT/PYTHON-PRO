n1=int(input('Qual a nota 1? '))
n2=int(input('Qual a nota 2? '))
media = (n1+n2)/2
print()
print('A media do aluno é',media)
if media > 60:
    print('Parabés! A aluno foi aprovado')
else:
    print('Que pena! A aluno foi reprovado')