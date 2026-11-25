# Aula 06 | Exercício 2 | Maior e menor de 5 pesos

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f"Peso {i} (kg)? "))
    if i == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f"Maior peso: {maior:.1f} kg")
print(f"Menor peso: {menor:.1f} kg")
