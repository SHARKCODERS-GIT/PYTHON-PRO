import requests

url = requests.get('https://economia.awesomeapi.com.br/last/EUR-USD')
cotacao = url.json()

cotacao_dolar = float(cotacao['EURUSD']['bid'])
valor = int(input('Qual o valor em Dolares deseja converter? '))
r = valor / cotacao_dolar
print('O valor convertido é de',round(r,2),'euros')