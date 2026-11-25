# Aula 01 | Extra 1 | Preço com IVA
# Entrada: preço sem IVA
# Saída: valor do IVA (23%) e preço final

preco = float(input("Preço sem IVA (€)? "))

iva = preco * 0.23
final = preco + iva

print("IVA (23%):", round(iva, 2), "€")
print("Preço final:", round(final, 2), "€")
