# Aula 05 | Extra 2 | Fatorial

n = int(input("Número? "))
fatorial = 1

for i in range(1, n + 1):
    fatorial = fatorial * i

print(n, "! =", fatorial)
