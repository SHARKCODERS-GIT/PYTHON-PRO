# Aula 09 | Exercício 5 | Calculadora de IMC

def calcular_imc(peso, altura):
    return peso / altura ** 2

def classificar(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"

peso = float(input("Peso (kg)? "))
altura = float(input("Altura (m)? "))
imc = calcular_imc(peso, altura)
print(f"IMC: {imc:.1f} · {classificar(imc)}")
