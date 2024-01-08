import sqlite3
#Ranking de novelas com mais horas consumidas por mês

def format_hour(tempo):
    tempo_h = int(tempo - (tempo % 1))
    tempo_m = int(((tempo % 1)*60) - ((tempo % 1)*60 % 1))
    tempo_s = round((((tempo % 1)*60) % 1)*60)
    return f"{tempo_h} horas {tempo_m} minutos {tempo_s} segundos"

def question2():
    print("2 - Ranking de novelas com mais horas consumidas por mês\n")
    meses = set()
    db = sqlite3.connect('registros.db')
    cursor = db.cursor()
  
    cursor.execute("""SELECT co.id_conteudo, co.data, co.horas_consumidas
                      FROM consumo co
                      JOIN conteudo c ON co.id_conteudo = c.id_conteudo
                      WHERE c.categoria = 'novela';
""")
    response = cursor.fetchall()
    print("O valor retornado da query é: ", response, "\n")
  
    #Iterando os registros e adicionando os meses ao conjunto
    for registro in response:
        data = registro[1]
        mes = data.split('/')[1]
        meses.add(mes)

    for mes in meses:
        lista_registros_mes = []
        set_novelas = set()
        novelas_horas_totais = []
        print("\nRanking do mês: ", mes)
        for registro in response:
            #adicionar registro que seja do mes do for numa lista
            if registro[1].split('/')[1] == mes:
                lista_registros_mes.append(registro)

        #Iterando a lista de registros do mes e adicionando as novelas ao conjunto
        for registro in lista_registros_mes:
            id_novela = registro[0]
            set_novelas.add(id_novela)

        str_novelas = str(set_novelas).replace("{", "").replace("}", "").replace("'", "")
        print("Novelas assistidas esse mês (exibido o id): ", str_novelas)

        for novela in set_novelas:
            horas_consumidas = 0
            for registro in lista_registros_mes:
                if registro[0] == novela:
                    horas_consumidas += float(registro[2])
            novelas_horas_totais.append((novela, horas_consumidas))
        print("Contagem de tempo de tela das novelas esse mês: ")
        for novela in novelas_horas_totais:
            print("A novela ", novela[0], "teve o total: ", format_hour(novela[1]), "de tempo de tela")

        ht_n_1 = novelas_horas_totais[0][1]
        if len(novelas_horas_totais) > 1:
            if novelas_horas_totais[0][1] > (ht_n_2 := novelas_horas_totais[1][1]):
                print("A novela mais consumida esse mês foi: ", novelas_horas_totais[0][0], " com ", format_hour(ht_n_1), "de tempo tela!!")
            else:
                print("A novela mais consumida esse mês foi: ", novelas_horas_totais[1][0], " com ", format_hour(ht_n_2), "de tempo tela!!")
        else:
            print("A novela mais consumida esse mês foi: ", novelas_horas_totais[0][0], " com ", format_hour(ht_n_1), "de tempo de tela!!")