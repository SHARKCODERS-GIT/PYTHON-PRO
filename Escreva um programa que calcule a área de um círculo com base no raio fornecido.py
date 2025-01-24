import math

def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

raio = float(input("Informe o raio do círculo: "))
area = calcular_area_circulo(raio)
print(f"A área do círculo com raio {raio} é: {area:.2f}")