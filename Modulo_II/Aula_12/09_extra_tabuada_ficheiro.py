# Aula 12 | Extra 3 | Tabuada para ficheiro

n = int(input("Tabuada do? "))

with open(f"tabuada_{n}.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(f"{n} x {i} = {n * i}\n")

print(f"Tabuada guardada em tabuada_{n}.txt")
