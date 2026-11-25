# Aula 11 | Extra 5 | Inverter um dicionário

capitais = {"Portugal": "Lisboa", "Espanha": "Madrid", "França": "Paris"}

paises = {capital: pais for pais, capital in capitais.items()}
print(paises)
print(paises["Madrid"])
