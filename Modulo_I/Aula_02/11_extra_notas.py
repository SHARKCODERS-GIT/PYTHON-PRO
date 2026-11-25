# Aula 02 | Extra 5 | Notas e moedas

valor = int(input("Valor a levantar (€)? "))

n50 = valor // 50
resto = valor % 50
n20 = resto // 20
resto = resto % 20
n10 = resto // 10
resto = resto % 10
n5 = resto // 5
resto = resto % 5

print("Notas de 50 €:", n50)
print("Notas de 20 €:", n20)
print("Notas de 10 €:", n10)
print("Notas de 5 €:", n5)
print("Sobra:", resto, "€")
