# Aula 11 | Exercício 3 | Tabela de proteínas

proteinas = {
    "Frango": 31, "Ovo": 13, "Atum": 30,
    "Lentilhas": 9, "Iogurte grego": 10, "Amêndoas": 21,
}

print(f"{'Alimento':<15}{'Proteína':>10}")
for alimento, g in sorted(proteinas.items()):
    print(f"{alimento:<15}{g:>8} g")
