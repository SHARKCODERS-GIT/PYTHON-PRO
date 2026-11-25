# Aula 15 | Exercício 4 | Conversor EUR → USD

import requests

url = "https://api.frankfurter.dev/v1/latest?from=EUR&to=USD"
dados = requests.get(url).json()
taxa = dados["rates"]["USD"]

euros = float(input("Valor em euros? "))
print(f"Taxa de {dados['date']}: 1 € = {taxa} $")
print(f"{euros:.2f} € = {euros * taxa:.2f} $")
