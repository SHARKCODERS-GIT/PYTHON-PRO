# Aula 15 | Extra 3 | Tabela de câmbios

import requests

dados = requests.get("https://api.frankfurter.dev/v1/latest?from=EUR&to=USD,GBP,BRL,CHF").json()

print(f"Taxas de {dados['date']} (1 €)")
for moeda, taxa in dados["rates"].items():
    print(f"{moeda}: {taxa:>8.4f}")
