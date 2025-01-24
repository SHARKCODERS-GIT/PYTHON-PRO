import sqlite3

# Conectar ou criar banco de dados
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Criar tabela de clientes
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    email TEXT NOT NULL)''')

# Funções para registrar, buscar e excluir clientes
def registrar_cliente(nome, telefone, email):
    cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()

def buscar_cliente(nome_ou_telefone):
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE ? OR telefone LIKE ?", ('%' + nome_ou_telefone + '%', '%' + nome_ou_telefone + '%'))
    return cursor.fetchall()

def excluir_cliente(id_cliente):
    cursor.execute("DELETE FROM clientes WHERE id=?", (id_cliente,))
    conn.commit()

# Exemplo de uso
registrar_cliente("Carlos Silva", "123456789", "carlos@gmail.com")
registrar_cliente("Maria Oliveira", "987654321", "maria@gmail.com")

print("Clientes cadastrados:")
for cliente in buscar_cliente("Carlos"):
    print(cliente)

# Excluir um cliente
excluir_cliente(1)

print("Clientes após exclusão:")
for cliente in buscar_cliente("Carlos"):
    print(cliente)

# Fechar conexão
conn.close()
