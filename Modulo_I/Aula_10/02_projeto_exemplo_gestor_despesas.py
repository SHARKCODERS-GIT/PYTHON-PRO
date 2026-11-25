# Aula 10 | Projeto de exemplo | Gestor de despesas

CATEGORIAS = ["Casa", "Transportes", "Alimentação", "Lazer"]

def ler_valor(pergunta):
    while True:
        try:
            valor = float(input(pergunta))
            if valor > 0:
                return valor
            print("O valor tem de ser positivo.")
        except ValueError:
            print("Escreva um número válido.")

def adicionar_despesa(despesas):
    descricao = input("Descrição? ").strip()
    print("Categorias:", ", ".join(CATEGORIAS))
    categoria = input("Categoria? ").strip().title()
    if categoria not in CATEGORIAS:
        categoria = "Outros"
    valor = ler_valor("Valor (€)? ")
    despesas.append([descricao, categoria, valor])
    print("Despesa registada.")

def listar(despesas):
    for i, (desc, cat, valor) in enumerate(despesas, 1):
        print(f"{i}. {desc:<12} {cat:<12} {valor:>8.2f} €")

def resumo(despesas):
    if len(despesas) == 0:
        print("Ainda não há despesas.")
        return
    valores = [d[2] for d in despesas]
    print(f"Total: {sum(valores):.2f} €")
    print(f"Média: {sum(valores) / len(valores):.2f} €")
    print(f"Maior: {max(valores):.2f} €")

despesas = []
while True:
    print("1 Adicionar | 2 Listar | 3 Resumo | 0 Sair")
    opcao = input("Opção? ")
    if opcao == "1":
        adicionar_despesa(despesas)
    elif opcao == "2":
        listar(despesas)
    elif opcao == "3":
        resumo(despesas)
    elif opcao == "0":
        print("Até à próxima!")
        break
    else:
        print("Opção inválida.")
