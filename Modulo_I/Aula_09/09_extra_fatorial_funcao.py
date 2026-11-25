# Aula 09 | Extra 3 | Fatorial

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

for n in range(1, 7):
    print(f"{n}! = {fatorial(n)}")
