# Aula 09 | Exercício 4 | Calculadora em ciclo

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "não é possível dividir por zero"
    return a / b

while True:
    print("1 + | 2 - | 3 x | 4 / | 0 Sair")
    opcao = input("Opção? ")
    if opcao == "0":
        print("Até à próxima!")
        break
    a = float(input("Número 1? "))
    b = float(input("Número 2? "))
    if opcao == "1":
        print("Resultado:", somar(a, b))
    elif opcao == "2":
        print("Resultado:", subtrair(a, b))
    elif opcao == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcao == "4":
        print("Resultado:", dividir(a, b))
    else:
        print("Opção inválida.")
