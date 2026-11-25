# Aula 12 | Extra 2 | Copiar um ficheiro

with open("3_linhas.txt", "r", encoding="utf-8") as origem:
    conteudo = origem.read()

with open("copia.txt", "w", encoding="utf-8") as destino:
    destino.write(conteudo)

print("Cópia criada com", len(conteudo), "caracteres.")
