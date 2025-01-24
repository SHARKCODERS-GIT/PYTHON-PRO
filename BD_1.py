import sqlite3

bd_loja = sqlite3.connect('loja_fic.db')
cursor = bd_loja.cursor()

print('=-'*16)
print('Sistema CRUD - Lojas Portuguesas')
print('=-'*16)

#menu
def menu():
    print('\n0 - Sair\n1 - Cadastrar Produto\n2 - Consultar Produtos\n3 - Modificar Produtos\n4 - Excluir Produtos')
    opc = int(input('Opção desejada: '))
    if opc == 1:
        print()
        create()


#CRUD - CREATE
def create():
    produto = input('Nome do produto: ')
    descricao = input('Descrição do produto: ')
    valor = float(input('Valor do produto: '))
    estoque = int(input('Quantidade em estoque: '))
    create = f'INSERT INTO tb_modelo (produto, descricao, valor, estoque) VALUES ("{produto}","{descricao}", "{valor}", "{estoque}")'
    cursor.execute(create)
    bd_loja.commit()


menu()
#Encerrar Cursor e conexão da BD
cursor.close()
bd_loja.close()