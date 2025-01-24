marca=input('Qual a marca do carro que deseja consultar? ')

if marca in 'Ford Chevrolet Dodge':
    print(marca,'é Americana')
elif marca in 'Honda Toyota Suzuki':
    print(marca, 'é Asiática')
elif marca in 'Peugeot Cintroen BMW':
    print(marca, 'é Europeia')
else:
    print ('Desculpa!',marca,'não consta em nossa Base de Dados.')