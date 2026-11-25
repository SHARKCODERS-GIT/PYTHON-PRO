# Aula 11 | Extra 4 | Votação

votos = {"A": 0, "B": 0, "C": 0}

for i in range(6):
    v = input("Voto (A/B/C)? ").strip().upper()
    if v in votos:
        votos[v] += 1

print(votos)
print("Vencedor:", max(votos, key=votos.get))
