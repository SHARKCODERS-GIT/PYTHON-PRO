# Aula 20 | Projeto de exemplo | Biblioteca pessoal

import sqlite3, csv

bd = sqlite3.connect("biblioteca.db")
bd.execute("""CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL,
    autor TEXT NOT NULL, ano INTEGER, lido INTEGER DEFAULT 0)""")

def ler_ano():
    while True:
        try:
            return int(input("Ano? "))
        except ValueError:
            print("Escreva um ano válido.")

def adicionar():
    titulo = input("Título? ").strip()
    autor = input("Autor? ").strip()
    if not titulo or not autor:
        print("Título e autor são obrigatórios."); return
    bd.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)", (titulo, autor, ler_ano()))
    bd.commit(); print("Livro adicionado.")

def listar(filtro=""):
    sql = "SELECT id, titulo, autor, ano, lido FROM livros WHERE titulo LIKE ? OR autor LIKE ?"
    for i, t, a, ano, lido in bd.execute(sql, (f"%{filtro}%", f"%{filtro}%")):
        print(f"{i:<3}{t:<28}{a:<20}{ano:<6}{'lido' if lido else 'por ler'}")

def marcar_lido():
    cur = bd.execute("UPDATE livros SET lido = 1 WHERE id = ?", (input("Id do livro? "),))
    bd.commit(); print("Marcado como lido." if cur.rowcount else "Livro não encontrado.")

def estatisticas():
    total, lidos = bd.execute("SELECT COUNT(*), SUM(lido) FROM livros").fetchone()
    if total:
        print(f"Livros: {total} · Lidos: {lidos} ({lidos / total:.0%})")

def exportar():
    with open("livros.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "titulo", "autor", "ano", "lido"])
        w.writerows(bd.execute("SELECT * FROM livros"))
    print("Exportado para livros.csv")

opcoes = {"1": adicionar, "2": listar, "3": lambda: listar(input("Pesquisar? ")),
          "4": marcar_lido, "5": estatisticas, "6": exportar}
print("1 Adicionar | 2 Listar | 3 Pesquisar | 4 Lido | 5 Estatísticas | 6 Exportar | 0 Sair")
while True:
    op = input("Opção? ")
    if op == "0":
        break
    opcoes.get(op, lambda: print("Opção inválida."))()
bd.close()
