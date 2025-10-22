"""
Streamlit application for Apriori Recommendation System.

This application provides an interactive interface to explore
transaction data and association rules.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from utils.data_loader import load_and_process_data, get_product_stats
from utils.visualization import plot_key_insights, plot_top_products, plot_order_distribution

# Page configuration
st.set_page_config(
    page_title="Apriori Recommendation System",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title('🛒 Sistema de Recomendaciones Personalizadas con Apriori y R')
st.markdown("""
Esta aplicación permite explorar patrones de compra en datos de transacciones de Instacart
utilizando el algoritmo Apriori para análisis de reglas de asociación.
""")
st.markdown("---")


@st.cache_data
def load_data():
    """Load and cache transaction data."""
    # Try multiple possible locations for the data file
    possible_paths = [
        'TransactionsInstacart.csv',
        'notebooks/TransactionsInstacart.csv',
        Path(__file__).parent / 'TransactionsInstacart.csv',
        Path(__file__).parent / 'notebooks' / 'TransactionsInstacart.csv'
    ]
    
    for path in possible_paths:
        try:
            return load_and_process_data(str(path))
        except FileNotFoundError:
            continue
    
    # If no file found, show error
    st.error("❌ No se pudo encontrar el archivo de datos. Por favor, asegúrate de que TransactionsInstacart.csv esté en el directorio correcto.")
    st.stop()


# Sidebar configuration
st.sidebar.header("⚙️ Configuración")
st.sidebar.markdown("Ajusta los parámetros de visualización")

# Load data
with st.spinner('Cargando datos...'):
    df = load_data()
    stats = get_product_stats(df)

# Show success message
st.success(f"✅ Datos cargados exitosamente: {stats['total_orders']:,} órdenes, {stats['total_products']:,} productos")

# Main content
st.header("📊 Principales hallazgos")

# Display key metrics in columns
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total de Órdenes", f"{stats['total_orders']:,}")
with col2:
    st.metric("Productos Únicos", f"{stats['total_products']:,}")
with col3:
    st.metric("Promedio Productos/Orden", f"{stats['avg_products_per_order']:.1f}")
with col4:
    st.metric("Mediana Productos/Orden", f"{stats['median_products_per_order']:.0f}")

st.markdown("---")

# Plot key insights
with st.spinner('Generando visualizaciones...'):
    fig = plot_key_insights(df)
    st.pyplot(fig)

# Additional visualizations
st.markdown("---")
st.header("📈 Análisis Detallado")

# Slider for top N products
top_n = st.sidebar.slider("Número de productos top a mostrar", 10, 50, 20)

# Create tabs for different visualizations
tab1, tab2 = st.tabs(["Productos Más Comprados", "Distribución de Órdenes"])

with tab1:
    st.subheader(f"Top {top_n} Productos Más Comprados")
    fig_top = plot_top_products(df, n=top_n)
    st.pyplot(fig_top)

with tab2:
    st.subheader("Distribución de Productos por Orden")
    fig_dist = plot_order_distribution(df)
    st.pyplot(fig_dist)

# Footer
st.markdown("---")
st.markdown("""
**Desarrollado por:** Fernanda Flores, Kevin Arciniegas, Giussepe Marreros  
**Institución:** 4Geeks Academy  
**Versión:** 1.1.0
""")

