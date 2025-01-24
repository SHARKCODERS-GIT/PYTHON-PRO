proteina = {'Soja':56,'Camarão':24,'Frango':23,'Peixes':20,'Leite':8}
print('-='*10)
print('Lista de Proteínas')
print('-='*10)
for x in sorted(proteina.items()):
    print(f'{x[0]} : {x[1]} de proteína a cada 100g')