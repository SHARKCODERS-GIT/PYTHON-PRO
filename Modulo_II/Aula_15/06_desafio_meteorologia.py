# Aula 15 | Desafio | Meteorologia em tempo real

import requests

cidades = {"porto": (41.15, -8.61), "lisboa": (38.72, -9.14),
           "faro": (37.02, -7.93), "braga": (41.55, -8.42)}

cidade = input("Cidade? ").strip().lower()
if cidade in cidades:
    lat, lon = cidades[cidade]
    url = ("https://api.open-meteo.com/v1/forecast"
           f"?latitude={lat}&longitude={lon}"
           "&current=temperature_2m,relative_humidity_2m,surface_pressure"
           "&daily=temperature_2m_max,temperature_2m_min&timezone=Europe/Lisbon")
    d = requests.get(url, timeout=10).json()
    print(f"{cidade.title()} · {d['current']['time']}")
    print(f"Temperatura atual: {d['current']['temperature_2m']} °C")
    print(f"Máxima: {d['daily']['temperature_2m_max'][0]} °C · Mínima: {d['daily']['temperature_2m_min'][0]} °C")
    print(f"Humidade: {d['current']['relative_humidity_2m']} %")
    print(f"Pressão: {d['current']['surface_pressure']} hPa")
else:
    print("Cidade não disponível.")
