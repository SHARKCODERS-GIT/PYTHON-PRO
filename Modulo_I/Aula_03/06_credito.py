# Aula 03 | Exercício 6 | Simulador de crédito habitação

salario = float(input("Salário líquido (€)? "))
emprestimo = float(input("Empréstimo (€)? "))
anos = int(input("Prazo (anos)? "))

prestacao = emprestimo / (anos * 12)
limite = salario * 0.35

print("Prestação mensal:", round(prestacao, 2), "€")
print("Limite (35%):", round(limite, 2), "€")
if prestacao <= limite:
    print("Crédito aprovado!")
else:
    print("Crédito recusado.")
