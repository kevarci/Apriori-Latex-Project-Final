import pandas as pd
import numpy as np
import re
import logging
from typing import List, Tuple, Dict
import os

# Configuración de logging senior
logger = logging.getLogger(__name__)

def clean_product_name(name: str) -> str:
    """
    Limpia el nombre del producto usando Regex para unificar el texto,
    siguiendo la lógica original del notebook pero optimizada.
    """
    if pd.isna(name):
        return ""
    # Reemplazar caracteres especiales por ~ para consistencia histórica del proyecto
    name = re.sub(r'[^a-zA-Z\d\s]+', '~', str(name))
    return name.lower().strip()

def load_and_group_transactions(orders_path: str, products_path: str) -> List[List[str]]:
    """
    Carga los datasets, realiza el merge y agrupa por order_id.
    Retorna una lista de listas (transacciones).
    """
    if not os.path.exists(orders_path) or not os.path.exists(products_path):
        logger.error(f"Uno o más archivos no existen: {orders_path}, {products_path}")
        raise FileNotFoundError("Verifica las rutas de los archivos CSV.")

    logger.info(f"Cargando datos desde {orders_path}...")
    try:
        orders = pd.read_csv(orders_path)
        products = pd.read_csv(products_path)
        
        # Limpieza senior de nombres
        logger.info("Normalizando nombres de productos...")
        products['product_name'] = products['product_name'].apply(clean_product_name)
        
        # Merge y ordenación (Optimizado)
        logger.info("Realizando merge de pedidos...")
        df_merged = pd.merge(orders, products, on="product_id", how="inner")
        df_merged.sort_values("order_id", inplace=True)
        
        # Agrupación eficiente
        logger.info("Agrupando transacciones por ID de pedido...")
        transactions = df_merged.groupby('order_id')['product_name'].apply(list).tolist()
        
        logger.info(f"Éxito: {len(transactions)} transacciones cargadas.")
        return transactions
    except Exception as e:
        logger.error(f"Error fatal en la carga de datos: {e}")
        raise

if __name__ == "__main__":
    # Prueba rápida de carga local
    logging.basicConfig(level=logging.INFO)
    TEST_ORDERS = 'c:/Users/pc/Desktop/Proyectos BigData/Apriori-Latex-Project-Final/data/raw/order_products__train.csv'
    TEST_PRODUCTS = 'c:/Users/pc/Desktop/Proyectos BigData/Apriori-Latex-Project-Final/data/raw/products.csv'
    try:
        data = load_and_group_transactions(TEST_ORDERS, TEST_PRODUCTS)
    except Exception as e:
        print(f"Error esperado en test si los archivos no existen en esta ruta: {e}")
