import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

from utils.data_loader import load_and_process_data
from utils.visualization import plot_key_insights

st.title('Sistema de Recomendaciones Personalizadas con Apriori y R')
st.markdown("---")

@st.cache_data

def load_data():
    return load_and_process_data('/workspaces/Apriori-Latex-Project-Final/notebooks/TransactionsInstacart.csv')

df = load_data()


st.header("Principales hallazgos")

fig = plot_key_insights(df)
st.pyplot(fig)


