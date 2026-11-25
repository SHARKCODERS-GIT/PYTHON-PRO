# Aula 15 | Exercício 5 | Conversor com menu

import requests

def taxa(origem, destino):
    url = f"https://api.frankfurter.dev/v1/latest?from={origem}&to={destino}"
    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        return None
    return r.json()["rates"][destino]

while True:
    par = input("Converter (ex.: EUR USD) ou 0 para sair? ").upper().split()
    if par == ["0"]:
        break
    if len(par) != 2:
        print("Escreva duas moedas, ex.: USD EUR")
        continue
    t = taxa(par[0], par[1])
    if t is None:
        print("Par de moedas inválido.")
        continue
    valor = float(input(f"Valor em {par[0]}? "))
    print(f"{valor:.2f} {par[0]} = {valor * t:.2f} {par[1]}")
