# Aula 06 | Exercício 5 | Calculadora de divisão segura

try:
    a = float(input("Dividendo? "))
    b = float(input("Divisor? "))
    print(f"{a} / {b} = {a / b:.2f}")
except ValueError:
    print("Erro: escreva números válidos.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
