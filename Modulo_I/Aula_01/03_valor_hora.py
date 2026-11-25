# Aula 01 | Exercício 3 | Valor por hora de um funcionário
# Entrada: salário mensal e horas de trabalho por mês
# Saída: valor por hora, arredondado a 2 casas decimais
# GitHub: Salario Hora.py

salario = float(input("Salário mensal (€)? "))
horas = float(input("Horas de trabalho por mês? "))

valor_hora = salario / horas

print("O valor por hora é", round(valor_hora, 2), "€")
