import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import pandas as pd
import os
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

def ensure_results_dir(path: str = "data/results"):
    if not os.path.exists(path):
        os.makedirs(path)

def plot_item_frequency(transactions: List[List[str]], top_n: int = 20, save_path: str = "data/results/item_frequency.png"):
    """
    Gráfica de barras con los productos más frecuentes.
    """
    ensure_results_dir()
    all_items = [item for sublist in transactions for item in sublist]
    df = pd.Series(all_items).value_counts().head(top_n).reset_index()
    df.columns = ['Product', 'Count']
    
    plt.figure(figsize=(12, 8))
    plt.barh(df['Product'], df['Count'], color='skyblue')
    plt.gca().invert_yaxis()
    plt.title(f"Top {top_n} Productos Más Frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(save_path)
    logger.info(f"Gráfica de frecuencia guardada en {save_path}")
    plt.close()

def plot_rules_scatter(rules: pd.DataFrame, title: str = "Análisis de Reglas de Asociación", save_path: str = "data/results/rules_scatter.html"):
    """
    Scatter plot interactivo de Soporte vs Confianza con tamaño por Lift.
    """
    ensure_results_dir()
    if rules.empty:
        logger.warning("No hay reglas para graficar en el scatter plot.")
        return

    # Convertir listas a strings para el hover de Plotly
    df_plot = rules.copy()
    df_plot['antecedent_str'] = df_plot['antecedent'].apply(lambda x: ", ".join(x))
    df_plot['consequent_str'] = df_plot['consequent'].apply(lambda x: ", ".join(x))

    fig = px.scatter(
        df_plot, 
        x="support", 
        y="confidence", 
        size="lift", 
        color="lift",
        hover_data=["antecedent_str", "consequent_str"],
        title=title,
        template="plotly_dark"
    )
    fig.write_html(save_path)
    logger.info(f"Scatter plot interactivo guardado en {save_path}")

def plot_rules_network(rules: pd.DataFrame, min_lift: float = 2.0, max_rules: int = 50, save_path: str = "data/results/rules_network.html"):
    """
    Grafo interactivo de asociaciones usando NetworkX y Plotly.
    """
    ensure_results_dir()
    if rules.empty:
        logger.warning("No hay reglas para graficar en la red.")
        return

    # Filtrar reglas significativas para evitar un grafo ilegible
    df = rules[rules['lift'] >= min_lift].head(max_rules)
    G = nx.DiGraph()

    for _, row in df.iterrows():
        ant = ", ".join(row['antecedent'])
        cons = ", ".join(row['consequent'])
        G.add_edge(ant, cons, weight=row['lift'], confidence=row['confidence'])

    pos = nx.spring_layout(G, k=0.5, iterations=50)

    # Nodos
    node_x = []
    node_y = []
    node_text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y, 
        mode='markers+text', 
        text=node_text,
        textposition="top center",
        hoverinfo='text',
        marker=dict(size=12, color='orange', line_width=2)
    )

    # Aristas (Conexiones)
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                 layout=go.Layout(
                    title='Red Interactiva de Reglas de Asociación',
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    template="plotly_dark"
                 ))
    fig.write_html(save_path)
    logger.info(f"Red de reglas guardada en {save_path}")

def plot_performance_comparison(bench_results: Dict[str, List[Dict]], save_path: str = "data/results/performance_comparison.png"):
    """
    Gráfica de líneas comparativa de tiempos de ejecución.
    """
    ensure_results_dir()
    plt.figure(figsize=(10, 6))
    
    for engine_name, trials in bench_results.items():
        df = pd.DataFrame(trials)
        # Agrupar por soporte y tomar el promedio si hay múltiples datasets
        df_avg = df.groupby('support')['time'].mean().reset_index()
        plt.plot(df_avg['support'], df_avg['time'], marker='o', label=engine_name)

    plt.title("Comparación de Rendimiento: Tiempo vs Soporte")
    plt.xlabel("Soporte Mínimo")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(save_path)
    logger.info(f"Gráfica de rendimiento guardada en {save_path}")
    plt.close()
