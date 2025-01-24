def gestor_de_notas():
    with open("notas.txt", "a") as ficheiro:
        while True:
            nota = input("Insira a nota do aluno (ou 'sair' para terminar): ")
            if nota.lower() == "sair":
                break
            try:
                nota = float(nota)
                ficheiro.write(f"{nota}\n")
            except ValueError:
                print("Valor inválido! Certifique-se de inserir um número.")

    with open("notas.txt", "r") as ficheiro:
        notas = [float(linha.strip()) for linha in ficheiro]
        if notas:
            media = sum(notas) / len(notas)
            print(f"Média das notas: {media:.2f}")
        else:
            print("Nenhuma nota registrada.")

gestor_de_notas()
