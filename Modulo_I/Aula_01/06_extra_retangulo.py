# Aula 01 | Extra 2 | Área e perímetro de um retângulo
# Entrada: comprimento e largura (metros)
# Saída: área e perímetro

comprimento = float(input("Comprimento (m)? "))
largura = float(input("Largura (m)? "))

area = comprimento * largura
perimetro = 2 * (comprimento + largura)

print("Área:", area, "m²")
print("Perímetro:", perimetro, "m")
