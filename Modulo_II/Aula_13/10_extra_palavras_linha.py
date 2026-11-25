# Aula 13 | Extra 4 | Contar palavras por linha

with open("frases.txt", encoding="utf-8") as f:
    for n, linha in enumerate(f, 1):
        print(f"Linha {n}: {len(linha.split())} palavras")
