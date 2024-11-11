import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

from datetime import datetime, timedelta

# Obtener la fecha de hoy
end =datetime.today().strftime('%Y-%m-%d')

# Restar un número de días (ejemplo: 365 días)
dias_a_restar = 30
start = (datetime.today() - timedelta(days=dias_a_restar)).strftime('%Y-%m-%d')

print("Fecha de inicio (start):", start)
print("Fecha de fin (end):", end)


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

ticker="CITY.MC"
int=yf.download(ticker, start, end)

fig, ax = plt.subplots()
int.Close.plot(kind='line', ax=ax)  # Puedes usar 'line', 'bar', 'scatter', etc.

st.pyplot(fig)