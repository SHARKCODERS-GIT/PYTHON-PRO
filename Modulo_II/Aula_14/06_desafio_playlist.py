# Aula 14 | Desafio | Playlist de rock clássico

import csv

with open("classic_rock_playlist.csv", encoding="utf-8") as f:
    musicas = list(csv.DictReader(f))

def pesquisar(campo, valor):
    res = [m for m in musicas if valor.lower() in m[campo].lower()]
    for m in res:
        print(f"{m['Artist']} · {m['Music']} · {m['Album']} · {m['Year']} · {m['Genre']}")
    print(len(res), "resultado(s).")

while True:
    op = input("1 Artista | 2 Música | 3 Ano | 0 Sair? ")
    if op == "0":
        break
    campos = {"1": "Artist", "2": "Music", "3": "Year"}
    if op in campos:
        pesquisar(campos[op], input("Pesquisa? "))
