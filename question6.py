import streamlit as st
import pandas as pd
import plotly.express as px
#6 - Conte uma história com os dados! Não precisa ser nada complexo. O objetivo é entendermos como você lida com informações e as analisa.


df = pd.read_csv("consumo.csv", sep=";", decimal=",")
df