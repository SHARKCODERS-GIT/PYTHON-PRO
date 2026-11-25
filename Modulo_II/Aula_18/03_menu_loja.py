# Aula 18 | Exercício 3 | Menu de registo

import sqlite3

conexao = sqlite3.connect("loja.db")

def registar():
    dados = (input("Produto? ").strip(), input("Descrição? ").strip(),
             float(input("Preço? ")), int(input("Stock? ")))
    try:
        conexao.execute("INSERT INTO produtos (produto, descricao, preco, stock) VALUES (?, ?, ?, ?)", dados)
        conexao.commit()
        print("Produto registado.")
    except sqlite3.IntegrityError:
        print("Esse produto já existe.")

def menu():
    while True:
        op = input("1 Registar produto | 0 Sair? ")
        if op == "1":
            registar()
        elif op == "0":
            break

menu()
conexao.close()
