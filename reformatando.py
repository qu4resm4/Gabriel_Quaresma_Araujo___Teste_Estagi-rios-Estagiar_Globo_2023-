import sqlite3
#Neste script vou reformatar os dados e mudar o seu tipo

#horas_consumidas from consumo
def reformat_hours(cursor):
    cursor.execute("""UPDATE consumo
                      SET horas_consumidas = REPLACE(horas_consumidas, ',', '.')""")

def reformatando():
    db = sqlite3.connect('registros.db')
    cursor = db.cursor()

    reformat_hours(cursor)

    db.commit()
    db.close()