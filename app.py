import streamlit  as st
import pandas as pd
import plotly_express as px

data = pd.read_csv('vehicles_us.csv')
hist_button = st.button("Construir histograma")
scatter_button = st.button("Construir grafico de dispersión")

if hist_button:
    st.header('Lanzar una moneda') #Encabezado
    st.write("construyendo un histograma") #Leyenda del histograma
    fig = px.histogram(data, x='odometer') #Creación del histograma
    st.plotly_chart(fig, use_container_width=True) #mostrar el histograma

if scatter_button:
    st.header("Lanzar una moneda") #Encabezado
    st.write("Creando el grafico de dispersion") #leyenda del scatter
    fig2 = px.scatter(data, x="odometer", y="price") #creación del scatter
    st.plotly_chart(fig2, use_container_width=True) #mostrar el scatter