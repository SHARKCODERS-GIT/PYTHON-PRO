# Aula 06 | Extra 1 | Recibo formatado

produto = input("Produto? ")
qtd = int(input("Quantidade? "))
preco = float(input("Preço unitário (€)? "))

print(f"{'Produto':<12}{'Qtd':>5}{'Total':>10}")
print(f"{produto:<12}{qtd:>5}{qtd * preco:>10.2f}")
