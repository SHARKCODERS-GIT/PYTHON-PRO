# Aula 06 | Exercício 1 | Tabuada formatada

n = int(input("Tabuada do? "))
for i in range(1, 11):
    print(f"{n} x {i:>2} = {n * i:>3}")
