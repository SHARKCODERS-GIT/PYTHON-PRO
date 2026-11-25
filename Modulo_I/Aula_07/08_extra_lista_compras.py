# Aula 07 | Extra 1 | Lista de compras

compras = []

while True:
    artigo = input("Artigo (fim para terminar)? ").strip().lower()
    if artigo == "fim":
        break
    compras.append(artigo)

compras.sort()
print(f"{len(compras)} artigos: {compras}")
