# Aula 03 | Extra 2 | O maior de três

a = float(input("Número 1? "))
b = float(input("Número 2? "))
c = float(input("Número 3? "))

if a >= b and a >= c:
    maior = a
elif b >= c:
    maior = b
else:
    maior = c

print("O maior é", maior)
