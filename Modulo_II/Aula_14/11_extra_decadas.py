# Aula 14 | Extra 5 | Músicas por década

import csv

decadas = {}
with open("classic_rock_playlist.csv", encoding="utf-8") as f:
    for m in csv.DictReader(f):
        d = int(m["Year"]) // 10 * 10
        decadas[d] = decadas.get(d, 0) + 1

for d in sorted(decadas):
    print(f"Anos {d}: {decadas[d]} músicas")
