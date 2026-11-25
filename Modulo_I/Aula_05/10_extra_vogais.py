# Aula 05 | Extra 3 | Contar vogais

frase = input("Frase? ")
vogais = 0

for c in frase:
    if c in "aeiouAEIOU":
        vogais = vogais + 1

print("Vogais:", vogais)
