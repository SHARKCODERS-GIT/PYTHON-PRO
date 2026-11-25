# Aula 14 | Exercício 4 | Registar uma venda

import csv
from datetime import date

produto = input("Produto? ").strip().title()
categoria = input("Categoria? ").strip().title()
quantidade = int(input("Quantidade? "))
preco = float(input("Preço unitário? "))

with open("vendas.csv", "a", newline="", encoding="utf-8") as f:
    csv.writer(f).writerow([date.today(), produto, categoria, quantidade, preco])
print("Venda registada.")
