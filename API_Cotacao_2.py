import requests

lista = ['EUR', 'USD', 'BRL']

print('=-'*10)
print('Conversor de Moedas')
print('=-'*10)

de = int(input('Qual a moeda de origem?\n0 - Euro\n1 - Dolar Americano\n2 - Real Brasileiro\nEscolha a opção: '))
de = lista[de]
print()
valor = int(input('Qual valor deseja converter: '))
print()
para = int(input('Para qual moeda deseja converter?\n0 - Euro\n1 - Dolar Americano\n2 - Real Brasileiro\nEscolha a opção: '))
para = lista[para]
print()

# request
cotacao = requests.get('https://economia.awesomeapi.com.br/last/{}'.format(de+'-'+para))
cotacao = cotacao.json()
cotacao_moeda = float(cotacao['{}'.format(de+para)]['bid'])

#formula

r = round(valor * cotacao_moeda,2)
print('O valor convertido é de',r,para)