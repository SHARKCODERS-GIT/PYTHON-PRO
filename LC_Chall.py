valores = [200, 810, 1500, 1800, 950, 450]

#Reajuste
reajuste = [valor * 1.25 for valor in valores]
print(f'Os valores reajustados são {reajuste}')

#Reajuste
impostos = [valor * 1.15 for valor in reajuste if valor > 1000]
print(f'Sobre os valores acima de 1000 euros, os valores com impostos são {impostos}')