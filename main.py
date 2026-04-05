import logging
import os
import pandas as pd
from utils.data_processing import load_and_group_transactions
from core.apriori_engine import AprioriHybridEngine, R_AVAILABLE, benchmark_engines
from utils.visualization import (
    plot_item_frequency, 
    plot_rules_scatter, 
    plot_rules_network, 
    plot_performance_comparison,
    ensure_results_dir
)

# Configuración de Logging Profesional
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    # 1. Definición de Rutas y Preparación de Resultados
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ORDERS_CSV = os.path.join(BASE_DIR, 'data', 'raw', 'order_products__train.csv')
    PRODUCTS_CSV = os.path.join(BASE_DIR, 'data', 'raw', 'products.csv')
    RESULTS_DIR = os.path.join(BASE_DIR, 'data', 'results')
    ensure_results_dir(RESULTS_DIR)

    logger.info("--- Iniciando Pipeline de Asociación Senior 100% ---")

    # 2. Carga de Datos Reales
    try:
        transactions = load_and_group_transactions(ORDERS_CSV, PRODUCTS_CSV)
        plot_item_frequency(transactions, top_n=30, save_path=f"{RESULTS_DIR}/item_frequency.png")
    except Exception as e:
        logger.error(f"Error cargando datos: {e}")
        return

    # 3. Inicialización del Motor de Producción
    engine = AprioriHybridEngine(transactions)

    # 4. Ejecución del Algoritmo con Selección del Mejor Motor
    if R_AVAILABLE:
        logger.info("Motor R detectado. Ejecutando Arules para resultados óptimos...")
        rules = engine.run_r_hybrid(min_support=0.005, min_confidence=0.3)
    else:
        logger.info("R no detectado. Utilizando Motor Python Manual (Optimizado para memoria)...")
        rules = engine.run_python_manual(min_support=0.01, min_confidence=0.3)

    # 5. Generación de Visualizaciones de Reglas Reales
    if not rules.empty:
        logger.info(f"Generadas {len(rules)} reglas. Creando visualizaciones interactivas...")
        rules.to_csv(f"{RESULTS_DIR}/main_rules.csv", index=False)
        plot_rules_scatter(rules, save_path=f"{RESULTS_DIR}/rules_scatter.html")
        plot_rules_network(rules, min_lift=2.5, max_rules=100, save_path=f"{RESULTS_DIR}/rules_network.html")
        
        # Ejemplo de recomendación senior
        sample_basket = ["organic raspberries", "organic whole milk"]
        recs = engine.get_recommendations(sample_basket, top_n=5)
        if not recs.empty:
            logger.info("Recomendaciones generadas exitosamente.")
            print("\n--- Recomendaciones sugeridas para el carrito ---")
            print(recs)
    
    # 6. Módulo de Comparación y Benchmarking (100% Notebook Sync)
    logger.info("--- Iniciando Benchmarking de Rendimiento ---")
    
    # Datasets sintéticos para pruebas de estrés
    small_data = AprioriHybridEngine.generate_synthetic_data(100, 20, 5)
    med_data = AprioriHybridEngine.generate_synthetic_data(1000, 50, 8)
    
    bench_datasets = {
        'Dataset Sintético Pequeño': small_data,
        'Dataset Sintético Mediano': med_data
    }
    
    bench_results = benchmark_engines(bench_datasets, min_supports=[0.1, 0.05, 0.02])
    plot_performance_comparison(bench_results, save_path=f"{RESULTS_DIR}/performance_comparison.png")
    
    # Comparativa con Fuerza Bruta (en dataset pequeño para evitar bloqueos)
    brute_engine = AprioriHybridEngine(small_data)
    logger.info("Evaluando Estrategia de Fuerza Bruta en dataset pequeño...")
    rules_brute = brute_engine.run_brute_force(min_support=0.05)
    logger.info(f"Fuerza Bruta completada: Encontrados {len(rules_brute)} itemsets.")

    logger.info("--- Pipeline Finalizado Exitosamente. Revisa la carpeta data/results/ ---")

if __name__ == "__main__":
    main()
