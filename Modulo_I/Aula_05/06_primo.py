# Aula 05 | Exercício 6 | Divisores e números primos

n = int(input("Número? "))
divisores = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        divisores = divisores + 1

print()
print(n, "tem", divisores, "divisores.")
if divisores == 2:
    print(n, "é primo.")
else:
    print(n, "não é primo.")
