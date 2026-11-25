# Aula 19 | Exercício 3 | Submenu de consulta

import sqlite3
c = sqlite3.connect("loja.db")

def todos():
    for prod, preco in c.execute("SELECT produto, preco FROM produtos ORDER BY produto"):
        print(f"{prod:<22}{preco:>8.2f} €")

def por_nome(texto):
    for prod, preco in c.execute("SELECT produto, preco FROM produtos WHERE produto LIKE ?", (f"%{texto}%",)):
        print(f"{prod:<22}{preco:>8.2f} €")

while True:
    op = input("Consultar: 1 Todos | 2 Por nome | 0 Voltar? ")
    if op == "1":
        todos()
    elif op == "2":
        por_nome(input("Nome? "))
    elif op == "0":
        break
c.close()
