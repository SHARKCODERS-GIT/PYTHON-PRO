# Aula 07 | Exercício 4 | Aceitar qualquer escrita

europa = ["Portugal", "Espanha", "França",
          "Itália", "Alemanha", "Bélgica"]

pais = input("Diga um país da Europa? ").strip().title()
if pais in europa:
    print("Parabéns!", pais, "está na lista.")
else:
    print(pais, "não está na lista.")
