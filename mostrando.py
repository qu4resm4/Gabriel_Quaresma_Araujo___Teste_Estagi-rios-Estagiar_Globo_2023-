import sqlite3

def print_table(table_name):
    db = sqlite3.connect('registros.db')
    cursor =db.cursor()

    cursor.execute(f'SELECT * FROM {table_name}')
    column_names = [column[0] for column in cursor.description]
    data = cursor.fetchall()

    print(f"\nDados da tabela {table_name}:\n")
    print(f"{', '.join(column_names)}")
    for row in data:
        print(row)

    db.close()
