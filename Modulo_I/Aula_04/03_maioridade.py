# Aula 04 | Exercício 3 | Idade e direitos

from datetime import date

nascimento = int(input("Ano de nascimento? "))
idade = date.today().year - nascimento

print("Tem (ou vai fazer este ano)", idade, "anos.")
if idade >= 18:
    print("Já pode votar e tirar a carta de condução.")
else:
    print("Faltam", 18 - idade, "anos para a maioridade.")
