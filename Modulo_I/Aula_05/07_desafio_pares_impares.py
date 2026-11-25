# Aula 05 | Desafio | Pares ou ímpares com soma

inicio = int(input("Início? "))
fim = int(input("Fim? "))
opcao = input("Pares ou ímpares (P/I)? ")
soma = 0

if opcao == "P":
    resto = 0
elif opcao == "I":
    resto = 1
else:
    resto = -1

if resto == -1:
    print("Opção inválida.")
else:
    for i in range(inicio, fim + 1):
        if i % 2 == resto:
            print(i, end=" ")
            soma = soma + i
    print()
    print("Soma:", soma)
