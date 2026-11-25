# Aula 07 | Exercício 5 | Três tentativas

europa = ["Portugal", "Espanha", "França",
          "Itália", "Alemanha", "Bélgica"]
acertou = False

for tentativa in range(1, 4):
    pais = input(f"Tentativa {tentativa}: país? ").strip().title()
    if pais in europa:
        print("Acertou!")
        acertou = True
        break
    print("Não está na lista.")

if not acertou:
    print("Esgotou as 3 tentativas.")
