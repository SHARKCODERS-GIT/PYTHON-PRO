maior = menor = 0

for n in range(1,6):
    num = int(input('Entre com o {}º peso: '.format(n)))
    if n == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print()
print("O número maior é:",maior)
print("O número menor é:",menor)