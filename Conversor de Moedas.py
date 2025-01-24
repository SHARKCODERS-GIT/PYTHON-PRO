import requests
import json

def conversor_de_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # API de exemplo
    ficheiro = "taxas_de_cambio.json"

    # Exemplo de estrutura do ficheiro 'taxas_de_cambio.json':
    # {
    #     "base": "USD",
    #     "date": "2025-01-24",
    #     "rates": {
    #         "EUR": 0.92,
    #         "GBP": 0.81,
    #         "JPY": 134.75
    #     }
    # }

    try:
        response = requests.get(url)
        response.raise_for_status()
        taxas = response.json()
        
        with open(ficheiro, "w") as f:
            json.dump(taxas, f, indent=4)
        
        print("Taxas de câmbio guardadas com sucesso!")
    except requests.RequestException as e:
        print(f"Erro ao obter taxas de câmbio: {e}")

    try:
        with open(ficheiro, "r") as f:
            dados = json.load(f)
            print("\nTaxas de Câmbio (Base: USD):")
            for moeda, taxa in dados["rates"].items():
                print(f"{moeda}: {taxa:.2f}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erro ao ler o ficheiro de taxas de câmbio.")

conversor_de_moedas()
