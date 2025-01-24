import requests

def previsao_do_tempo():
    api_key = "SUA_CHAVE_AQUI"  # Substitua por sua chave de API do OpenWeather
    url_base = "https://api.openweathermap.org/data/2.5/weather"

    cidade = input("Digite o nome da cidade: ").strip()
    
    try:
        parametros = {"q": cidade, "appid": api_key, "units": "metric", "lang": "pt"}
        response = requests.get(url_base, params=parametros)
        response.raise_for_status()
        dados = response.json()

        # Exemplo de dados retornados pela API:
        # {
        #     "weather": [{"description": "céu limpo"}],
        #     "main": {"temp": 28.5, "feels_like": 31.0, "temp_min": 25.0, "temp_max": 30.0},
        #     "name": "Lisboa",
        #     "sys": {"country": "PT"}
        # }

        print(f"\nPrevisão do tempo para {dados['name']}, {dados['sys']['country']}:")
        print(f"  Temperatura Atual: {dados['main']['temp']}°C")
        print(f"  Sensação Térmica: {dados['main']['feels_like']}°C")
        print(f"  Mínima: {dados['main']['temp_min']}°C")
        print(f"  Máxima: {dados['main']['temp_max']}°C")
        print(f"  Condição: {dados['weather'][0]['description'].capitalize()}")

    except requests.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
    except KeyError:
        print("Erro: Cidade não encontrada ou dados inválidos.")

previsao_do_tempo()
