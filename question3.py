import sqlite3
from datetime import datetime
#Conteúdo de primeiro play do usuário

def question3():
    print("3 - Conteúdo de primeiro play do usuário\n")
    set_user = set()
    db = sqlite3.connect('registros.db')
    cursor = db.cursor()

    cursor.execute("""SELECT id_user, id_conteudo, data
                          FROM consumo""")
    response = cursor.fetchall()
    print("O valor retornado da query é: ", response, "\n")

    #Listando users
    for registro in response:
        set_user.add(registro[0])

    #Iterando execução por users
    for user in set_user:
        lista_plays_user = []
        play_mais_antigo = None
        for registro in response:
            if user == registro[0]:
                lista_plays_user.append(registro)
        #print("LISTA DO USER", user, ":", lista_plays_user)

        for play in lista_plays_user:
            if play_mais_antigo == None:
                play_mais_antigo = play
              
            elif (d_play := datetime.strptime(play[2], "%d/%m/%Y")) < (d_play_m_a := datetime.strptime(play_mais_antigo[2], "%d/%m/%Y")):
                play_mais_antigo = play
        print("O conteúdo de primeiro play do usuário ", user, " é: ", play_mais_antigo[1])