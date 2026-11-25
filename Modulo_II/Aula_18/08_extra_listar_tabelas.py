# Aula 18 | Extra 3 | Listar tabelas

import sqlite3

c = sqlite3.connect("loja.db")
tabelas = [t[0] for t in c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
for t in tabelas:
    print(t, c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0], "linhas")
c.close()
