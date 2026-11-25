# Aula 10 | Modelo de projeto

# 1. Importações (se precisar)

# 2. Funções
def opcao_1(dados):
    print("Opção 1 em construção")

# 3. Programa principal
dados = []
while True:
    print("1 - Opção 1 | 0 - Sair")
    opcao = input("Escolha? ")
    if opcao == "1":
        opcao_1(dados)
    elif opcao == "0":
        print("Até à próxima!")
        break
    else:
        print("Opção inválida.")
