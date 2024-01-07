import sqlite3
import csv

def create_tables(cursor):
    #Cria tabela CONTEUDO se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conteudo (
            id_conteudo INTEGER PRIMARY KEY,
            conteudo TEXT,
            categoria TEXT
        )
    ''')

    #Cria tabela CONSUMO se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consumo (
            id_user INTEGER,
            id_conteudo INTEGER,
            data DATE,
            horas_consumidas FLOAT,
            FOREIGN KEY (id_conteudo) REFERENCES conteudo(id_conteudo)
        )
    ''')

def insert_data(cursor, csv_filename, table_name, columns):
    # Abre o arquivo CSV no modo de uso leitura ('r')
    with open(csv_filename, 'r') as csv_file:
        # Cria um leitor de dicionário e itera
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Verifica se todos os valores nas colunas especificadas são não nulos
            if all(row[column] for column in columns):
              # Consulta SQL dinamicamente usando f-strings
              query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in columns])})"
              # Cria uma tubla com os valores column da row para a quantidade de columns especificadas 
              values = tuple(row[column] for column in columns)
              
              cursor.execute(query, values)

def verify(cursor, table_name):
  # Verifica se a tabela está preenchida
  cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
  result = cursor.fetchone()[0]
  return result == 0

def main():
    # Conecta ao banco de dados, se não existir o cria
    db = sqlite3.connect('registros.db')
    cursor = db.cursor()

    # Cria as tabelas
    create_tables(cursor)

    # Insere os dados nas tabelas
    if verify(cursor, 'conteudo'):
        insert_data(cursor, 'conteudo.csv', 'conteudo', ['id_conteudo', 'conteudo', 'categoria'])
    if verify(cursor, 'consumo'):
        insert_data(cursor, 'consumo.csv', 'consumo', ['id_user', 'id_conteudo', 'data', 'horas_consumidas'])

    # Confirma as alterações e finaliza a conexão com o db
    db.commit()
    db.close()