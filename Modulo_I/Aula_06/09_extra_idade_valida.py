# Aula 06 | Extra 3 | Idade válida

while True:
    try:
        idade = int(input("Idade? "))
        break
    except ValueError:
        print("Escreva um número inteiro.")

print(f"Idade registada: {idade} anos")
