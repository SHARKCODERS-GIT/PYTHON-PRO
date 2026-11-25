# Aula 13 | Extra 1 | Numerar linhas

with open("agenda.txt", encoding="utf-8") as origem, open("agenda_numerada.txt", "w", encoding="utf-8") as destino:
    for n, linha in enumerate(origem, 1):
        destino.write(f"{n}. {linha}")

print(open("agenda_numerada.txt", encoding="utf-8").read())
