import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

import datetime as dt 

# Obtener la fecha de hoy
hoy =dt.datetime.today().strftime('%Y-%m-%d')

# Restar un número de días (ejemplo: 365 días)
dias_a_restar = 365
start = (dt.datetime.today() - dt.timedelta(days=dias_a_restar)).strftime('%Y-%m-%d')

print("Fecha de inicio (start):", start)
print("Fecha de fin (hoy):", hoy)


st.title("INTERCITY C.F.")
st.write("El equipo que te hará millonario")

ticker="CITY.MC"
int=yf.download(ticker, start, end=hoy)
st.write(int.head())

fig, ax = plt.subplots()
int.Close.plot(kind='line', ax=ax)  # Puedes usar 'line', 'bar', 'scatter', etc.

st.pyplot(fig)
