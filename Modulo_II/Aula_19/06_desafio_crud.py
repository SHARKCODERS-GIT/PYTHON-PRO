# Aula 19 | Desafio | CRUD completo da loja

import sqlite3

c = sqlite3.connect("loja.db")

def registar():
    dados = (input("Produto? "), input("Descrição? "), float(input("Preço? ")), int(input("Stock? ")))
    try:
        c.execute("INSERT INTO produtos (produto, descricao, preco, stock) VALUES (?, ?, ?, ?)", dados)
        c.commit(); print("Registado.")
    except sqlite3.IntegrityError:
        print("Produto já existe.")

def consultar():
    texto = input("Pesquisar (Enter para todos)? ")
    for p, preco, s in c.execute("SELECT produto, preco, stock FROM produtos WHERE produto LIKE ?", (f"%{texto}%",)):
        print(f"{p:<22}{preco:>8.2f} € {s:>4}")

def atualizar():
    cur = c.execute("UPDATE produtos SET preco = ? WHERE produto = ?", (float(input("Novo preço? ")), input("Produto? ")))
    c.commit(); print("Atualizado." if cur.rowcount else "Não encontrado.")

def apagar():
    produto = input("Produto? ")
    if input(f"Apagar {produto}? (s/n) ").lower() == "s":
        cur = c.execute("DELETE FROM produtos WHERE produto = ?", (produto,))
        c.commit(); print("Apagado." if cur.rowcount else "Não encontrado.")

opcoes = {"1": registar, "2": consultar, "3": atualizar, "4": apagar}
while True:
    op = input("1 Registar | 2 Consultar | 3 Atualizar | 4 Apagar | 0 Sair? ")
    if op == "0":
        break
    opcoes.get(op, lambda: print("Opção inválida."))()
c.close()
