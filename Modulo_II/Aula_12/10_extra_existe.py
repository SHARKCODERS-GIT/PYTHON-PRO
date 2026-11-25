# Aula 12 | Extra 4 | O ficheiro existe?

import os

nome = input("Nome do ficheiro? ")
if os.path.exists(nome):
    print(nome, "existe.")
else:
    print(nome, "não existe.")
