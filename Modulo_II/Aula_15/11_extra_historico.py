# Aula 15 | Extra 5 | Histórico de conversões

import json, os

registo = {"de": "EUR", "para": "USD", "valor": 100, "resultado": 109.63}

historico = []
if os.path.exists("historico.json"):
    with open("historico.json", encoding="utf-8") as f:
        historico = json.load(f)
historico.append(registo)

with open("historico.json", "w", encoding="utf-8") as f:
    json.dump(historico, f, indent=2)
print("Conversões guardadas:", len(historico))
