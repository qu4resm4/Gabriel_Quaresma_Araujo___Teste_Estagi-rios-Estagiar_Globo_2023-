import sqlite3
#Minutos por play para cada usuário

def question4():
    print("4 - Minutos por play para cada usuário\n")
    db = sqlite3.connect('registros.db')
    cursor = db.cursor()

    cursor.execute("""SELECT co.id_user,
                      AVG(CAST(horas_consumidas 
                      AS FLOAT)) AS media_horas_consumidas
                      FROM consumo co 
                      GROUP BY co.id_user""")
    media_user = cursor.fetchall()
    print("O valor retornado da query é: ", media_user, "\n")

    for user in media_user:
        media = user[1]
        minutos = media*60
        print("A média de minutos assistidos por reproduções do usuário", user[0], " é, aproximadamente: ", round(minutos), "minutos por play\n")