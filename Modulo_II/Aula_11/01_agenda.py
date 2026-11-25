# Aula 11 | Exercício 1 | Agenda de contactos

agenda = {
    "Ana": "912 345 678",
    "Rui": "936 543 210",
    "Inês": "965 111 222",
}

def consultar(nome):
    return agenda.get(nome, "Contacto não encontrado.")

nome = input("Nome a consultar? ").strip().title()
print(consultar(nome))
