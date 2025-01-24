import csv

def analise_de_dados():
    temperaturas = []

    try:
        with open("caminho\\temperaturas.csv", "r") as ficheiro:
            leitor = csv.reader(ficheiro)
            for linha in leitor:
                try:
                    temperaturas.append(float(linha[0]))
                except ValueError:
                    print(f"Valor inválido ignorado: {linha[0]}")

        if temperaturas:
            media = sum(temperaturas) / len(temperaturas)
            maxima = max(temperaturas)
            minima = min(temperaturas)

            print("\nAnálise de Temperaturas:")
            print(f"Média: {media:.2f}")
            print(f"Máxima: {maxima:.2f}")
            print(f"Mínima: {minima:.2f}")
        else:
            print("Nenhuma temperatura válida foi encontrada.")

    except FileNotFoundError:
        print("O ficheiro 'temperaturas.csv' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o ficheiro: {str(e)}")

analise_de_dados()
