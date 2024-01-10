# -*- coding: utf-8 -*-
"""Laurie  Streamlit_build_data_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rJIOKdcvyZM19FZBy46Wbg0-1WAs3ZC9
"""

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Hello Wilders, welcome to my application!')
st.write("I enjoy to discover stremalit possibilities")
name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
st.write(df_cars)

# Apply filters to DataFrame
selected_continent = "Europe.", "Japan.", "US."
filtered_df = df_cars[df_cars["continent"] == selected_continent]
st.write('Filtered Data:')
st.write(filtered_df)

st.title('Analyse de corrélation')
st.pyplot(sns.heatmap(df_cars.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True)).figure)

st.title('Analyse de distribution')
st.line_chart(df_cars, x="year", y="mpg")

st.title('Analyse temporelle')
st.bar_chart(df_cars, x="year", y="hp")

#filterer les données en fonction de la region sélectionnés
def filtrer_par_continent(continent):
 if continent =='Tous':
    return df
    return df[df['continent'] == continent]

# creer le heatmap
st.title('analyser de corrélation et de distribution')
st.sidebar.header('Filter par continent')
selected_continent = st.sidebar.selectbox("selectionner un continent", ['Tous']+df['continent'].unique().tolist())

#filter les données en fonction des données selectionner
data_filtred = filtrer_par_continent(selected_continent)

# afficher les permier lignes des données
st.write("apercu des données:")
st.write(data_filtred.head())

# analyser de correlation
st.write("matrice de corrélation")
corr_matrix = data_filtred.corr()
st.write(corr_matrix.style.background_gradient(cmap='coolwarm'))

# Distribution des colonnes numériques
st.write("Distribution des colonnes numériques:")
for col in data_filtred.select_dtypes(include=['float64', 'int64']).columns:
    st.write(f"**{col}**:")
    fig, ax = plt.subplots()
    sns.histplot(data_filtred[col], kde=True, ax=ax)
    st.pyplot(fig)

# Affichage des boutons de filtrage par continent
st.write("Boutons de filtrage par continent:")
continents = ['Tous'] + df['continent'].unique().tolist()
for continent in continents:
    button_clicked = st.button(continent)
    if button_clicked:
        selected_continent = continent
        data_filtered = filtrer_par_continent(selected_continent)

# Affichage du footer
st.markdown()