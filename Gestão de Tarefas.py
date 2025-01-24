import sqlite3

# Conectar ou criar banco de dados
conn = sqlite3.connect("tarefas.db")
cursor = conn.cursor()

# Criar tabela de tarefas
cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    descricao TEXT,
                    status TEXT NOT NULL)''')

# Funções para criar, listar, atualizar e apagar tarefas
def criar_tarefa(titulo, descricao, status="pendente"):
    cursor.execute("INSERT INTO tarefas (titulo, descricao, status) VALUES (?, ?, ?)", (titulo, descricao, status))
    conn.commit()

def listar_tarefas():
    cursor.execute("SELECT * FROM tarefas")
    return cursor.fetchall()

def atualizar_status_tarefa(id_tarefa, status):
    cursor.execute("UPDATE tarefas SET status=? WHERE id=?", (status, id_tarefa))
    conn.commit()

def apagar_tarefa(id_tarefa):
    cursor.execute("DELETE FROM tarefas WHERE id=?", (id_tarefa,))
    conn.commit()

# Exemplo de uso
criar_tarefa("Estudar Python", "Estudar tópicos de Python para aprender SQLite", "pendente")
criar_tarefa("Comprar leite", "Comprar leite na loja", "concluída")

print("Tarefas atuais:")
for tarefa in listar_tarefas():
    print(tarefa)

# Atualizar o status de uma tarefa
atualizar_status_tarefa(1, "concluída")

# Apagar uma tarefa
apagar_tarefa(2)

print("Tarefas após atualizações:")
for tarefa in listar_tarefas():
    print(tarefa)

# Fechar conexão
conn.close()
