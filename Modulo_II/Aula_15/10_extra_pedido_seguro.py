# Aula 15 | Extra 4 | Pedido protegido

import requests

try:
    r = requests.get("https://api.frankfurter.dev/v1/latest?from=EUR&to=GBP", timeout=10)
    if r.status_code == 200:
        print("1 € =", r.json()["rates"]["GBP"], "£")
    else:
        print("Erro na API:", r.status_code)
except requests.exceptions.RequestException:
    print("Sem ligação à internet.")
