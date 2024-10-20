import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
st.header('Visualización de datos')

hist_checkbox = st.checkbox('Construir histograma')  # crear un botón
if hist_checkbox:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig1 = px.histogram(car_data, x="odometer", )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

scatter_checkbox = st.checkbox('Contruir un gráfico de dispersión')
if scatter_checkbox:

    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un scatterplot
    fig2 = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)