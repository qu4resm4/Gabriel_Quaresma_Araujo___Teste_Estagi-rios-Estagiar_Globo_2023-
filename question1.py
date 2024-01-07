import sqlite3
#Quantidade de horas consumidas e plays por categoria

def hours_quantity(cursor):
    cursor.execute("""SELECT SUM(CAST(REPLACE(horas_consumidas, ',', '.') 
                      AS FLOAT)) 
                      FROM consumo;""")
    
    total = cursor.fetchone()[0]
    print("O valor retornado da query é: ", total)
  
    total_h = int(total - (total % 1))
    total_m = int(((total % 1)*60) - ((total % 1)*60 % 1))
    total_s = round((((total % 1)*60) % 1)*60)

    print("O total de horas consumidas aproximadamente, é: ", total_h, "horas ", total_m, "minutos ", total_s, "segundos")

def plays_category(cursor):
    cursor.execute("""SELECT c.categoria, COUNT(*) AS quantidade_registros
                      FROM conteudo c
                      JOIN consumo co ON c.id_conteudo = co.id_conteudo
                      GROUP BY c.categoria;""")
    plays = cursor.fetchall()
    print("O valor retornado da query é: ", plays)
    for categoria in plays:
        quantidade = categoria[1]
        print("A quantidade de plays por categoria", categoria[0], "é :", quantidade)


def question1():
    db = sqlite3.connect('registros.db')
    cursor =db.cursor()
    
    #Quantidade total de horas consumidas
    hours_quantity(cursor)

    #Plays por categoria
    plays_category(cursor)

    db.close()