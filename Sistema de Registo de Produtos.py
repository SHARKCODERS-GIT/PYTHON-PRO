import sqlite3

# Conectar ou criar banco de dados
conn = sqlite3.connect("produtos.db")
cursor = conn.cursor()

# Criar tabela de produtos
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    preco REAL NOT NULL)''')

# Funções para registrar, atualizar e excluir produtos
def registrar_produto(nome, quantidade, preco):
    cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)", (nome, quantidade, preco))
    conn.commit()

def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    return cursor.fetchall()

def atualizar_produto(id_produto, nome, quantidade, preco):
    cursor.execute("UPDATE produtos SET nome=?, quantidade=?, preco=? WHERE id=?", (nome, quantidade, preco, id_produto))
    conn.commit()

def excluir_produto(id_produto):
    cursor.execute("DELETE FROM produtos WHERE id=?", (id_produto,))
    conn.commit()

# Exemplo de uso
registrar_produto("Produto A", 100, 20.50)
registrar_produto("Produto B", 50, 10.75)

print("Produtos cadastrados:")
for produto in listar_produtos():
    print(produto)

# Atualizar um produto
atualizar_produto(1, "Produto A", 150, 18.99)

# Excluir um produto
excluir_produto(2)

print("Produtos após atualizações:")
for produto in listar_produtos():
    print(produto)

# Fechar conexão
conn.close()
