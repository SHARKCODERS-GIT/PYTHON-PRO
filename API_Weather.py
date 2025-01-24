import requests

print('=-'*7)
print('Global Weather')
print('=-'*7)
print()
city = input('Qual cidade deseja verificar: ')
print()

apikey = 'aba304e1b88c4bbeff3e1524ea015a8b'

url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang=pt_br')
weather = url.json()

temp_k = weather['main']['temp']
temp_c = round(temp_k - 273.15, 1)

localizacao = weather['name']
pais = weather['sys']['country']

print(f'No momento faz {temp_c}ºC em {city} - {pais}')