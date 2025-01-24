n = int(input("Digite o número de termos: "))
soma = 0
for x in range(1, n + 1):
    soma += x
    print(x,end=' ')

print()
print('A soma de todos os números é',soma)