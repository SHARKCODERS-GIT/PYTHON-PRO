# Aula 06 | Extra 4 | Tabela de IVA

print(f"{'Preço':>8}{'IVA':>8}{'Total':>9}")
for preco in range(10, 51, 10):
    iva = preco * 0.23
    print(f"{preco:>8.2f}{iva:>8.2f}{preco + iva:>9.2f}")
