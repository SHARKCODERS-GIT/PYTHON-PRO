# Aula 19 | Extra 3 | Aumento geral de preços

import sqlite3

c = sqlite3.connect("loja.db")
cur = c.execute("UPDATE produtos SET preco = ROUND(preco * 1.05, 2)")
c.commit()
print(cur.rowcount, "preços atualizados.")
print(c.execute("SELECT produto, preco FROM produtos LIMIT 2").fetchall())
c.close()
