import sqlite3
from pathlib import Path
##Este código em Python implementa um sistema simples de controle de estoque utilizando o banco de dados SQLite. Ele permite ao usuário adicionar, remover, atualizar a quantidade e listar produtos em um banco de dados

ROOT_DIR = Path(__file__).parent
DB_NAME = 'minha_loja.db'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'estoque_fisico'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


cursor.execute(
    
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'produto TEXT NOT NULL, '
    'quantidade INTEGER NOT NULL'
    ')'
)




def menu_inicial():
    print("BEM VINDO AO CONTROLE DE ESTOQUE!!!")
    print("1 - Adicionar Produtos\n")
    print("2 - Remover Produtos\n")
    print("3 - Atualizar Quantidade\n")
    print("4 - Listar Produtos\n")
    print("5 - Sair\n")
    
    opcao = int(input("OPCAO: "))
    return opcao
    
def adicionar_produto(nome, quantidade):
    cursor.execute(
        'INSERT INTO estoque_fisico (produto, quantidade)'
        'VALUES (?,?)',
        (nome, quantidade)
    )
    connection.commit()
    print("Produto adicionado ao estoque_fisico com sucesso!!!")
    
def listar_produtos():
    cursor.execute(
        'SELECT * FROM estoque_fisico'
    )
    for row in cursor.fetchall():
        numero_id,produto,quantidade = row
        print(f'ID: {numero_id}     Produto: {produto}     Quantidade: {quantidade}') 
        
def atualizar_quantidade(id_produto,nova_quantidade):
    cursor.execute(
        'UPDATE estoque_fisico '
        'SET quantidade = ?'
        'WHERE id = ?',
        (nova_quantidade, id_produto)
    )      
    connection.commit()
    print("Quantidade atualizada com sucesso!!!")

def remover_produto(id_produto):
    cursor.execute(
        'DELETE from estoque_fisico '
        'WHERE id = ?',
        (id_produto,)     
    )
    connection.commit()
    print("Produto removido com sucesso!!!")

while True:
    entrada = ' '
    opcao_escolhida = menu_inicial()

    if opcao_escolhida == 1:
        adicionar_produto(input('Nome do Produto: '), int(input('Quantidade do Produto: ')))
        
        while entrada.upper() != 'M' and entrada.upper() != 'S':
            entrada= input("M - Menu\nS - Sair\n")
        if entrada.upper() == 'M':
            continue
        elif entrada.upper() == 'S':
            break   

    elif opcao_escolhida == 2:
        remover_produto(int(input('ID do produto: ')))
        
        while entrada.upper() != 'M' and entrada.upper() != 'S':
            entrada= input("M - Menu\nS - Sair\n")
        if entrada.upper() == 'M':
            continue
        elif entrada.upper() == 'S':
            break   
    elif opcao_escolhida == 3:
        atualizar_quantidade(int(input("ID do produto: ")),int(input("Nova Quantidade: ")))
        
        while entrada.upper() != 'M' and entrada.upper() != 'S':
            entrada= input("M - Menu\nS - Sair\n")
        if entrada.upper() == 'M':
            continue
        elif entrada.upper() == 'S':
            break   
    elif opcao_escolhida == 4:
        listar_produtos()
        
        while entrada.upper() != 'M' and entrada.upper() != 'S':
            entrada= input("M - Menu\nS - Sair\n")
        if entrada.upper() == 'M':
            continue
        elif entrada.upper() == 'S':
            break   
    elif opcao_escolhida == 5:
        break
    
    else:
        print("Opção Inexistente!")

        while entrada.upper() != 'M' and entrada.upper() != 'S':
            entrada= input("M - Menu\nS - Sair\n")
        if entrada.upper() == 'M':
            continue
        elif entrada.upper() == 'S':
            break 