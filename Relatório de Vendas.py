import csv
from collections import defaultdict

def relatorio_de_vendas():
    vendas = defaultdict(float)

    try:
        with open("caminho\\vendas.csv", "r") as ficheiro:
            leitor = csv.reader(ficheiro)
            for linha in leitor:
                produto, quantidade, valor = linha[0], int(linha[1]), float(linha[2])
                vendas[produto] += quantidade * valor

        print("\nRelatório de Vendas:")
        for produto, total in vendas.items():
            print(f"Produto: {produto}, Total Vendido: {total:.2f}")

    except FileNotFoundError:
        print("O ficheiro 'vendas.csv' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o ficheiro: {str(e)}")

relatorio_de_vendas()
