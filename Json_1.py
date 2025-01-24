import json

with open('Dados.json', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    print('Empresa 1\nFuncionária:',dados['emp1']['name'],
          '\nCargo:',dados['emp1']['designation'],
          '\nIdade:',dados['emp1']['age'],
          '\nSalario Anual:',dados['emp1']['salary'])