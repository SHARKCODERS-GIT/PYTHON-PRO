# Aula 13 | Extra 3 | Filtrar maiores de idade

with open("idades.txt", encoding="utf-8") as f, open("adultos.txt", "w", encoding="utf-8") as out:
    for linha in f:
        nome, idade = linha.strip().split(";")
        if int(idade) >= 25:
            out.write(linha)

print(open("adultos.txt", encoding="utf-8").read().strip())
