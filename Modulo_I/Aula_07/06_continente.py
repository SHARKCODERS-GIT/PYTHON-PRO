# Aula 07 | Exercício 6 | Em que continente fica?

europa = ["Portugal", "Espanha", "França", "Itália"]
asia = ["Japão", "China", "Índia", "Tailândia"]
africa = ["Angola", "Moçambique", "Marrocos", "Egito"]

pais = input("País? ").strip().title()
if pais in europa:
    print(pais, "fica na Europa.")
elif pais in asia:
    print(pais, "fica na Ásia.")
elif pais in africa:
    print(pais, "fica em África.")
else:
    print(pais, "não consta na base de dados.")
