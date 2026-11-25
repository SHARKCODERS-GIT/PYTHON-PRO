# Aula 03 | Exercício 5 | Aumento salarial por escalões

salario = float(input("Salário atual (€)? "))

if salario <= 1000:
    taxa = 10
elif salario <= 2000:
    taxa = 7
else:
    taxa = 5

novo = salario + salario * taxa / 100
print("Aumento de", taxa, "%")
print("Novo salário:", round(novo, 2), "€")
