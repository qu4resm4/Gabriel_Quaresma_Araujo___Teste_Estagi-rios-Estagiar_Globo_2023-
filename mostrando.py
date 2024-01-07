import sqlite3

def mostrar_dados_tabela(nome_tabela):
    # Conectar ao banco de dados
    conn = sqlite3.connect('registros.db')
    cursor = conn.cursor()

    # Consultar todos os dados da tabela
    cursor.execute(f'SELECT * FROM {nome_tabela}')
    dados = cursor.fetchall()

    # Exibir os dados
    print(f"\nDados da tabela {nome_tabela}:\n")
    for linha in dados:
        print(linha)

    # Fechar a conexão
    conn.close()
