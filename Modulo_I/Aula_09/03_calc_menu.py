# Aula 09 | Exercício 3 | Calculadora com menu

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

print("1 - Somar")
print("2 - Subtrair")
opcao = input("Opção? ")
a = float(input("Número 1? "))
b = float(input("Número 2? "))

if opcao == "1":
    print("Resultado:", somar(a, b))
elif opcao == "2":
    print("Resultado:", subtrair(a, b))
else:
    print("Opção inválida.")
