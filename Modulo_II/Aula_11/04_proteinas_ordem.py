# Aula 11 | Exercício 4 | Ordenar à escolha

proteinas = {
    "Frango": 31, "Ovo": 13, "Atum": 30,
    "Lentilhas": 9, "Iogurte grego": 10, "Amêndoas": 21,
}

ordem = input("Ordem alfabética (A) ou proteica (P)? ").strip().upper()
if ordem == "P":
    chaves = sorted(proteinas, key=proteinas.get, reverse=True)
else:
    chaves = sorted(proteinas)

for alimento in chaves:
    print(f"{alimento:<15}{proteinas[alimento]:>4} g")
