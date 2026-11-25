# Aula 13 | Extra 5 | Substituir uma palavra

with open("frases.txt", encoding="utf-8") as f:
    texto = f.read()

novo = texto.replace("Python", "PYTHON")
with open("frases_novas.txt", "w", encoding="utf-8") as f:
    f.write(novo)

print("Substituições:", texto.count("Python"))
