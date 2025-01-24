from datetime import date

hoje=date.today().year
nasc=int(input('Qual o ano de nascimento do jovem? '))
idade=hoje-nasc
prazo = 18-idade
print()
if idade<=17:
    print('Ainda não esta no prazo de alistamento militar. Ainda lhe falta', prazo,'anos.')
else:
    print('Já esta no prazo de alistamento militar. Estas atrasado em', (-prazo),'anos.')