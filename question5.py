import sqlite3
#Qual a categoria mais consumida para cada usuário

def question5():
    print("5 - Qual a categoria mais consumida para cada usuário\n")
    ids_usuarios = set()
    db = sqlite3.connect('registros.db')
    cursor = db.cursor()

    cursor.execute("""SELECT co.id_user, c.categoria, COUNT(*) AS quantidade_registros
                      FROM conteudo c
                      JOIN consumo co ON c.id_conteudo = co.id_conteudo
                      GROUP BY co.id_user, c.categoria;""")

    matriz = cursor.fetchall()
    print("O valor retornado da query é: ", matriz, "\n")

    #Iterando sobre as tuplas e adicionando os IDs ao conjunto
    for tupla in matriz:
        id_usuario = tupla[0]
        ids_usuarios.add(id_usuario)
      
    #Criando uma matriz para armazenar a contagem de cada categoria de cada usuário
    for id_usuario in ids_usuarios:
        #Cria uma lista com as tuplas do respectivo usuário
        user_tuplas = [tupla for tupla in matriz if tupla[0] == id_usuario]
        if len(user_tuplas) > 1:
            print("\nPlays do usuário", id_usuario, "por categoria: ", user_tuplas[0][2], " por ", user_tuplas[0][1], " e ", user_tuplas[1][2], " por ", user_tuplas[1][1])
        else:
          print("\nPlays do usuário", id_usuario, "por categoria: ", user_tuplas[0][2], " por ", user_tuplas[0][1])
      
        #Compara qual das categoria foi mais assistida pelo user
        primeiro_elemento = user_tuplas[0]
        for tupla in user_tuplas:
            #Pula a primeira tupla
            if tupla[2] == primeiro_elemento[2]:
                continue
            
            #Se for maior que a primeira
            if tupla[2] > primeiro_elemento[2]:
                print("A categoria mais consumida pelo usuário ", id_usuario, " é: ", tupla[1])
            else:
                print("A categoria mais consumida pelo usuário ", id_usuario, " é: ", primeiro_elemento[1])