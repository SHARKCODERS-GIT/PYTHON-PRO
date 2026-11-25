# Aula 04 | Extra 4 | Média de notas até -1

soma = 0
quantidade = 0

while True:
    nota = float(input("Nota (-1 para terminar)? "))
    if nota == -1:
        break
    soma = soma + nota
    quantidade = quantidade + 1

print("Notas:", quantidade)
print("Média:", round(soma / quantidade, 1))
