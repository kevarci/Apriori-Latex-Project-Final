"""
Data loader module for Apriori recommendation system.

This module provides functions to load and process transaction data
from Instacart dataset for use in Apriori algorithm analysis.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_and_process_data(filepath, min_products=2, max_products=50):
    """
    Load and process transaction data from CSV file.
    
    Args:
        filepath (str): Path to the CSV file containing transaction data
        min_products (int): Minimum number of products per order (default: 2)
        max_products (int): Maximum number of products per order (default: 50)
        
    Returns:
        pd.DataFrame: Processed dataframe with transaction data
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        ValueError: If the data format is invalid
    """
    try:
        # Convert to Path object for better path handling
        filepath = Path(filepath)
        
        # Check if file exists
        if not filepath.exists():
            # Try alternative paths (relative to project root)
            project_root = Path(__file__).parent.parent
            alternative_paths = [
                project_root / 'notebooks' / filepath.name,
                project_root / filepath.name,
                Path('notebooks') / filepath.name,
                Path(filepath.name)
            ]
            
            for alt_path in alternative_paths:
                if alt_path.exists():
                    filepath = alt_path
                    logger.info(f"Found data file at: {filepath}")
                    break
            else:
                raise FileNotFoundError(
                    f"Could not find data file. Searched in: {[str(p) for p in alternative_paths]}"
                )
        
        logger.info(f"Loading data from: {filepath}")
        
        # Load the CSV file
        df = pd.read_csv(filepath)
        
        # Validate required columns
        required_columns = ['order_id', 'product_name']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(
                f"Data must contain columns: {required_columns}. "
                f"Found: {list(df.columns)}"
            )
        
        # Remove missing values
        df = df.dropna(subset=required_columns)
        
        # Filter orders by product count
        order_counts = df.groupby('order_id').size()
        valid_orders = order_counts[
            (order_counts >= min_products) & (order_counts <= max_products)
        ].index
        
        df = df[df['order_id'].isin(valid_orders)]
        
        logger.info(f"Loaded {len(df)} transactions from {len(df['order_id'].unique())} orders")
        logger.info(f"Found {len(df['product_name'].unique())} unique products")
        
        return df
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except ValueError as e:
        logger.error(f"Invalid data format: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise


def get_transaction_matrix(df):
    """
    Convert transaction dataframe to a binary matrix format.
    
    Args:
        df (pd.DataFrame): Dataframe with order_id and product_name columns
        
    Returns:
        pd.DataFrame: Binary matrix where rows are orders and columns are products
    """
    try:
        # Create a pivot table with binary values
        matrix = pd.crosstab(df['order_id'], df['product_name'])
        
        # Convert to binary (0 or 1)
        matrix = (matrix > 0).astype(int)
        
        logger.info(f"Created transaction matrix: {matrix.shape[0]} orders x {matrix.shape[1]} products")
        
        return matrix
        
    except Exception as e:
        logger.error(f"Error creating transaction matrix: {e}")
        raise


def get_top_products(df, n=20):
    """
    Get the top N most frequently purchased products.
    
    Args:
        df (pd.DataFrame): Dataframe with product_name column
        n (int): Number of top products to return (default: 20)
        
    Returns:
        pd.Series: Series with product names and their counts
    """
    try:
        top_products = df['product_name'].value_counts().head(n)
        logger.info(f"Retrieved top {n} products")
        return top_products
        
    except Exception as e:
        logger.error(f"Error getting top products: {e}")
        raise


def get_product_stats(df):
    """
    Get statistical summary of products in the dataset.
    
    Args:
        df (pd.DataFrame): Dataframe with transaction data
        
    Returns:
        dict: Dictionary containing various statistics
    """
    try:
        stats = {
            'total_orders': df['order_id'].nunique(),
            'total_products': df['product_name'].nunique(),
            'total_transactions': len(df),
            'avg_products_per_order': df.groupby('order_id').size().mean(),
            'median_products_per_order': df.groupby('order_id').size().median(),
            'min_products_per_order': df.groupby('order_id').size().min(),
            'max_products_per_order': df.groupby('order_id').size().max()
        }
        
        logger.info("Generated product statistics")
        return stats
        
    except Exception as e:
        logger.error(f"Error getting product stats: {e}")
        raise


def prepare_for_apriori(df, format='list'):
    """
    Prepare transaction data for Apriori algorithm.
    
    Args:
        df (pd.DataFrame): Dataframe with order_id and product_name columns
        format (str): Output format - 'list' or 'matrix' (default: 'list')
        
    Returns:
        list or pd.DataFrame: Transactions in the specified format
    """
    try:
        if format == 'list':
            # Group products by order_id into lists
            transactions = df.groupby('order_id')['product_name'].apply(list).tolist()
            logger.info(f"Prepared {len(transactions)} transactions as lists")
            return transactions
            
        elif format == 'matrix':
            # Return binary matrix
            return get_transaction_matrix(df)
            
        else:
            raise ValueError(f"Invalid format: {format}. Use 'list' or 'matrix'")
            
    except Exception as e:
        logger.error(f"Error preparing data for Apriori: {e}")
        raise
