# Aula 18 | Extra 2 | Validar o preço

while True:
    try:
        preco = float(input("Preço? "))
        if preco > 0:
            break
        print("O preço tem de ser positivo.")
    except ValueError:
        print("Escreva um número.")

print(f"Preço aceite: {preco:.2f} €")
