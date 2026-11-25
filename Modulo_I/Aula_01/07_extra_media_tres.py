# Aula 01 | Extra 3 | Média de três notas
# Entrada: três notas
# Saída: média arredondada a 1 casa decimal

n1 = float(input("Nota 1? "))
n2 = float(input("Nota 2? "))
n3 = float(input("Nota 3? "))

media = (n1 + n2 + n3) / 3

print("Média final:", round(media, 1))
