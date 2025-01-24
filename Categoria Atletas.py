from datetime import date

hoje=date.today().year
nasc=int(input('Qual o ano de nascimento do atleta? '))
idade=hoje-nasc
print()
if idade<=9:
    print('Este atleta é da base Mirin')
elif idade<=14:
    print('Este atleta é da base Infantil')
elif idade<=19:
    print('Este atleta é da base Junior')
elif idade<=25:
    print('Este atleta é da base Senior')
else:
    print('Este atleta é da base Master')