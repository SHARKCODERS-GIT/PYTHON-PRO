# Aula 09 | Extra 5 | Desconto por quantidade

def preco_final(preco, quantidade):
    total = preco * quantidade
    if quantidade >= 10:
        total = total * 0.9
    return total

print(f"5 unidades: {preco_final(2.5, 5):.2f} €")
print(f"12 unidades: {preco_final(2.5, 12):.2f} €")
