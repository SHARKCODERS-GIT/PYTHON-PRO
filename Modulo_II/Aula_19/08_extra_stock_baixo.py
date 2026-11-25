# Aula 19 | Extra 2 | Stock baixo

import sqlite3

c = sqlite3.connect("loja.db")
for p, s in c.execute("SELECT produto, stock FROM produtos WHERE stock < ?", (5,)):
    print(f"Atenção: {p} só tem {s} unidades.")
c.close()
