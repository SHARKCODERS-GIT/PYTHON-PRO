# Aula 11 | Exercício 2 | Agenda com menu

agenda = {
    "Ana": "912 345 678",
    "Rui": "936 543 210",
    "Inês": "965 111 222",
}

def adicionar(nome, numero):
    agenda[nome] = numero

def apagar(nome):
    if nome in agenda:
        agenda.pop(nome)
    else:
        print("Contacto não existe.")

while True:
    op = input("1 Consultar | 2 Adicionar | 3 Apagar | 0 Sair? ")
    if op == "0":
        break
    nome = input("Nome? ").strip().title()
    if op == "1":
        print(agenda.get(nome, "Contacto não encontrado."))
    elif op == "2":
        adicionar(nome, input("Número? "))
    elif op == "3":
        apagar(nome)
    print("Contactos:", ", ".join(agenda))
