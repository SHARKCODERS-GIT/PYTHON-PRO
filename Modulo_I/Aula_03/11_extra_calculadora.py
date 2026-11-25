# Aula 03 | Extra 4 | Calculadora simples

a = float(input("Número 1? "))
b = float(input("Número 2? "))
op = input("Operação (+ - * /)? ")

if op == "+":
    print("Resultado:", a + b)
elif op == "-":
    print("Resultado:", a - b)
elif op == "*":
    print("Resultado:", a * b)
elif op == "/" and b != 0:
    print("Resultado:", a / b)
elif op == "/":
    print("Não é possível dividir por zero.")
else:
    print("Operação inválida.")
