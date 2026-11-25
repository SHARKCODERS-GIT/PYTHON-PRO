# Aula 07 | Extra 4 | Remover duplicados

unicos = []

for i in range(6):
    nome = input("Nome? ").strip().title()
    if nome not in unicos:
        unicos.append(nome)

print("Sem repetidos:", unicos)
