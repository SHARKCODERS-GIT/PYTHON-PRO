import requests

def consulta_de_moedas():
    url_base = "https://economia.awesomeapi.com.br/json/last/"

    print("Consulta de Moedas:")
    print("Exemplo de pares: USD-BRL, EUR-USD, BTC-USD")
    pares = input("Digite os pares de moedas (separados por vírgula): ").strip()

    try:
        response = requests.get(url_base + pares.replace(" ", ""))
        response.raise_for_status()
        dados = response.json()
        
        # Exemplo de dados retornados pela API:
        # {
        #     "USDBRL": {
        #         "code": "USD",
        #         "codein": "BRL",
        #         "name": "Dólar Americano/Real Brasileiro",
        #         "high": "5.43",
        #         "low": "5.37",
        #         "bid": "5.40",
        #         "ask": "5.42",
        #         "timestamp": "1618578670",
        #         "create_date": "2023-01-24 09:00:00"
        #     }
        # }

        for par, info in dados.items():
            print(f"\nCotação para {info['name']}:")
            print(f"  Alta: {info['high']}")
            print(f"  Baixa: {info['low']}")
            print(f"  Compra: {info['bid']}")
            print(f"  Venda: {info['ask']}")

    except requests.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
    except KeyError:
        print("Erro: Um ou mais pares de moedas são inválidos.")

consulta_de_moedas()
