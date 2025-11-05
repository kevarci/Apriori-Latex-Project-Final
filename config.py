"""
Configuration file for Apriori Recommendation System.

This module contains configuration constants and settings
used throughout the application.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / 'data'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'
DOCS_DIR = PROJECT_ROOT / 'docs'
UTILS_DIR = PROJECT_ROOT / 'utils'

# Data file paths
TRANSACTIONS_FILE = os.getenv('TRANSACTIONS_FILE', 'TransactionsInstacart.csv')
PRODUCTS_FILE = os.getenv('PRODUCTS_FILE', 'products.csv')
ORDERS_FILE = os.getenv('ORDERS_FILE', 'order_products__train.csv')

# Apriori algorithm parameters
MIN_SUPPORT = float(os.getenv('MIN_SUPPORT', '0.01'))
MIN_CONFIDENCE = float(os.getenv('MIN_CONFIDENCE', '0.3'))
MIN_LIFT = float(os.getenv('MIN_LIFT', '1.0'))

# Data processing parameters
MIN_PRODUCTS_PER_ORDER = int(os.getenv('MIN_PRODUCTS_PER_ORDER', '2'))
MAX_PRODUCTS_PER_ORDER = int(os.getenv('MAX_PRODUCTS_PER_ORDER', '50'))

# Visualization parameters
DEFAULT_TOP_N = int(os.getenv('DEFAULT_TOP_N', '20'))
FIGURE_DPI = int(os.getenv('FIGURE_DPI', '100'))

# Streamlit configuration
STREAMLIT_PORT = int(os.getenv('STREAMLIT_PORT', '8501'))
STREAMLIT_HOST = os.getenv('STREAMLIT_HOST', 'localhost')

# Logging configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Application metadata
APP_NAME = "Apriori Recommendation System"
APP_VERSION = "1.1.0"
APP_DESCRIPTION = "Sistema de Recomendaciones Personalizadas con Apriori y R"
APP_AUTHORS = ["Fernanda Flores", "Kevin Arciniegas", "Giussepe Marreros"]
APP_INSTITUTION = "4Geeks Academy"
