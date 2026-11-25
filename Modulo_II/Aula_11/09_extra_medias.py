# Aula 11 | Extra 3 | Médias por aluno

notas = {"Ana": [15, 17, 16], "Rui": [12, 11, 14], "Inês": [18, 19, 17]}

for aluno, lista in notas.items():
    print(f"{aluno}: {sum(lista) / len(lista):.1f}")
