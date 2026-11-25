# Aula 02 | Exercício 4 | Tinta para uma parede

largura = float(input("Largura da parede (m)? "))
altura = float(input("Altura da parede (m)? "))

area = largura * altura
litros = area / 2

print("Área da parede:", area, "m²")
print("Tinta necessária:", litros, "litros")
