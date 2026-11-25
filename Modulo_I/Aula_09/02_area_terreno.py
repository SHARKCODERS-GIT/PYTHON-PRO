# Aula 09 | Exercício 2 | Área de um terreno

def area(largura, comprimento):
    return largura * comprimento

l = float(input("Largura (m)? "))
c = float(input("Comprimento (m)? "))
print(f"Área do terreno: {area(l, c):.2f} m²")
