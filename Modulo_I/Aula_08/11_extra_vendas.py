# Aula 08 | Extra 4 | Vendas acima da média

vendas = [320, 410, 280, 515, 390, 600, 250]
media = sum(vendas) / len(vendas)
acima = [v for v in vendas if v > media]

print(f"Média: {media:.2f} €")
print("Acima da média:", acima)
