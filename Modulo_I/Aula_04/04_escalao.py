# Aula 04 | Exercício 4 | Escalão desportivo

from datetime import date

nascimento = int(input("Ano de nascimento do atleta? "))
idade = date.today().year - nascimento

if idade <= 9:
    escalao = "Benjamim"
elif idade <= 14:
    escalao = "Infantil"
elif idade <= 19:
    escalao = "Júnior"
elif idade <= 35:
    escalao = "Sénior"
else:
    escalao = "Veterano"

print("Idade:", idade, "anos · Escalão:", escalao)
