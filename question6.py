import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
import subprocess


# Função para conectar ao banco de dados SQLite e carregar dados
def load_data():
    conn = sqlite3.connect('registros.db')  # Substitua 'seu_banco_de_dados.db' pelo nome do seu arquivo .db
    query = """
        SELECT c.*, co.categoria
        FROM consumo c
        JOIN conteudo co ON c.id_conteudo = co.id_conteudo
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Página principal
def question6():
    df = load_data()

    st.title("Dashboard de Consumo")

    # Mostrar uma tabela com os dados
    st.subheader("Dados do Consumo")
    st.write(df)

    # Gráfico de Barras para a Quantidade de Horas Consumidas por Categoria
    st.subheader("Quantidade de Horas Consumidas por Categoria")
    fig_horas_categoria = px.bar(df, x='categoria', y='horas_consumidas', color='categoria', title='Horas Consumidas por Categoria')
    st.plotly_chart(fig_horas_categoria)

    # Executa o comando streamlit run main.py
    subprocess.run(['streamlit', 'run', 'main.py'])