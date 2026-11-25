# Aula 04 | Exercício 1 | Área de um círculo

from math import pi

raio = float(input("Raio (cm)? "))
area = pi * raio ** 2

print("A área do círculo é", round(area, 2), "cm²")
