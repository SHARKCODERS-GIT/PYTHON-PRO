# Aula 12 | Extra 5 | Lista de compras guardada

with open("compras.txt", "w", encoding="utf-8") as f:
    while True:
        artigo = input("Artigo (fim para terminar)? ")
        if artigo.lower() == "fim":
            break
        f.write(artigo + "\n")

with open("compras.txt", "r", encoding="utf-8") as f:
    print(f.read())
