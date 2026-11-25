# Aula 03 | Extra 5 | Portes de envio

total = float(input("Valor da encomenda (€)? "))
destino = input("Destino (C/I)? ")

if total > 50:
    portes = 0
elif destino == "C":
    portes = 3.99
else:
    portes = 7.50

print("Portes:", portes, "€")
print("Total:", round(total + portes, 2), "€")
