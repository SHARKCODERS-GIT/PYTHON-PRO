# Aula 04 | Exercício 5 | Contagem decrescente

from time import sleep

n = int(input("Começar a contagem em? "))

while n >= 0:
    print(n)
    sleep(1)
    n = n - 1

print("Descolagem!")
