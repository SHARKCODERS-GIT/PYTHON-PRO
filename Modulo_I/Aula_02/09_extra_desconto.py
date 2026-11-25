# Aula 02 | Extra 3 | Desconto em loja

preco = float(input("Preço do artigo (€)? "))
percentagem = float(input("Desconto (%)? "))

desconto = preco * percentagem / 100
final = preco - desconto

print("Desconto:", round(desconto, 2), "€")
print("Preço final:", round(final, 2), "€")
