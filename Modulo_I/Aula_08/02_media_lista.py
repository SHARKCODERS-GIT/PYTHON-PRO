# Aula 08 | Exercício 2 | Média com lista

numeros = []

while True:
    n = float(input("Número (0 para terminar)? "))
    if n == 0:
        break
    numeros.append(n)

print("Números:", numeros)
if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    print(f"Soma: {sum(numeros)} · Média: {media:.2f}")
else:
    print("Não foram introduzidos números.")
