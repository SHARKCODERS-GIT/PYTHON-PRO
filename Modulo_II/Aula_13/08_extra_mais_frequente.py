# Aula 13 | Extra 2 | Palavra mais frequente

contagem = {}
with open("frases.txt", encoding="utf-8") as f:
    for linha in f:
        for p in linha.lower().replace(".", "").split():
            if len(p) > 3:
                contagem[p] = contagem.get(p, 0) + 1

mais = max(contagem, key=contagem.get)
print(f"{mais}: {contagem[mais]} vezes")
