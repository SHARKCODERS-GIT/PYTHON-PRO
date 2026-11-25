# Aula 06 | Desafio | Média de números até zero

soma = 0
quantidade = 0

while True:
    try:
        n = int(input("Número inteiro (0 para terminar)? "))
    except ValueError:
        print("Valor inválido, tente de novo.")
        continue
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1

try:
    print(f"Números: {quantidade} · Média: {soma / quantidade:.2f}")
except ZeroDivisionError:
    print("Não foram introduzidos números.")
