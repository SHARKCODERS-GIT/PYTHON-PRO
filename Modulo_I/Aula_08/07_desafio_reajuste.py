# Aula 08 | Desafio | Reajuste de preços e impostos

precos = [12.0, 45.5, 8.9, 120.0, 33.3, 64.0]

reajustados = [round(p * 1.25, 2) for p in precos]
com_iva = [round(p * 1.23, 2) for p in reajustados]

print("Originais:  ", precos)
print("Reajustados:", reajustados)
print("Com IVA:    ", com_iva)
print(f"Total original: {sum(precos):.2f} €")
print(f"Total final: {sum(com_iva):.2f} €")
