import csv

def registo_de_alunos():
    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Visualizar registos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            idade = input("Idade do aluno: ")
            nota = input("Nota do aluno: ")

            with open("alunos.csv", "a", newline="") as ficheiro:
                escritor = csv.writer(ficheiro)
                escritor.writerow([nome, idade, nota])
            print("Aluno adicionado com sucesso!")

        elif opcao == "2":
            try:
                with open("alunos.csv", "r") as ficheiro:
                    leitor = csv.reader(ficheiro)
                    print("\nRegistos de Alunos:")
                    for linha in leitor:
                        print(f"Nome: {linha[0]}, Idade: {linha[1]}, Nota: {linha[2]}")
            except FileNotFoundError:
                print("Ainda não há registos de alunos.")

        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

registo_de_alunos()
