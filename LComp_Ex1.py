valores = [200, 700, 1500, 1800, 100, 35]

#For
n_valores = []
for valor in valores:
    n_valores.append(valor * 2)
print(n_valores)

#LComp
n2_valores = [valor * 2 for valor in valores]
print(n2_valores)