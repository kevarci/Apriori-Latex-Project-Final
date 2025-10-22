"""
Visualization module for Apriori recommendation system.

This module provides functions to create various visualizations
for transaction data and association rules analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def plot_key_insights(df, top_n=20):
    """
    Create a comprehensive visualization of key insights from transaction data.
    
    Args:
        df (pd.DataFrame): Dataframe with transaction data
        top_n (int): Number of top products to display (default: 20)
        
    Returns:
        matplotlib.figure.Figure: Figure object containing the plots
    """
    try:
        logger.info("Generating key insights visualization")
        
        # Create figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Key Insights - Instacart Transaction Analysis', 
                     fontsize=16, fontweight='bold')
        
        # Plot 1: Top N most purchased products
        top_products = df['product_name'].value_counts().head(top_n)
        axes[0, 0].barh(range(len(top_products)), top_products.values, color='steelblue')
        axes[0, 0].set_yticks(range(len(top_products)))
        axes[0, 0].set_yticklabels(top_products.index, fontsize=9)
        axes[0, 0].set_xlabel('Number of Purchases', fontsize=11)
        axes[0, 0].set_title(f'Top {top_n} Most Purchased Products', fontsize=12, fontweight='bold')
        axes[0, 0].invert_yaxis()
        
        # Add value labels
        for i, v in enumerate(top_products.values):
            axes[0, 0].text(v + 0.5, i, str(v), va='center', fontsize=8)
        
        # Plot 2: Distribution of products per order
        products_per_order = df.groupby('order_id').size()
        axes[0, 1].hist(products_per_order, bins=30, color='coral', edgecolor='black', alpha=0.7)
        axes[0, 1].set_xlabel('Number of Products per Order', fontsize=11)
        axes[0, 1].set_ylabel('Frequency', fontsize=11)
        axes[0, 1].set_title('Distribution of Products per Order', fontsize=12, fontweight='bold')
        axes[0, 1].axvline(products_per_order.mean(), color='red', linestyle='--', 
                           linewidth=2, label=f'Mean: {products_per_order.mean():.1f}')
        axes[0, 1].axvline(products_per_order.median(), color='green', linestyle='--', 
                           linewidth=2, label=f'Median: {products_per_order.median():.1f}')
        axes[0, 1].legend()
        
        # Plot 3: Orders over time (if date column exists)
        if 'order_dow' in df.columns:
            orders_by_day = df.groupby('order_dow')['order_id'].nunique()
            day_names = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
            axes[1, 0].bar(range(7), orders_by_day.values, color='lightgreen', edgecolor='black')
            axes[1, 0].set_xticks(range(7))
            axes[1, 0].set_xticklabels(day_names)
            axes[1, 0].set_xlabel('Day of Week', fontsize=11)
            axes[1, 0].set_ylabel('Number of Orders', fontsize=11)
            axes[1, 0].set_title('Orders by Day of Week', fontsize=12, fontweight='bold')
        else:
            # Alternative: Show product category distribution if available
            axes[1, 0].text(0.5, 0.5, 'Order timing data not available', 
                           ha='center', va='center', fontsize=12, transform=axes[1, 0].transAxes)
            axes[1, 0].set_title('Orders by Day of Week (N/A)', fontsize=12, fontweight='bold')
        
        # Plot 4: Summary statistics
        stats_text = f"""
        Dataset Summary Statistics:
        
        • Total Orders: {df['order_id'].nunique():,}
        • Total Products: {df['product_name'].nunique():,}
        • Total Transactions: {len(df):,}
        
        • Avg Products/Order: {products_per_order.mean():.2f}
        • Median Products/Order: {products_per_order.median():.0f}
        • Min Products/Order: {products_per_order.min():.0f}
        • Max Products/Order: {products_per_order.max():.0f}
        
        • Most Popular Product: {top_products.index[0]}
          ({top_products.values[0]:,} purchases)
        """
        
        axes[1, 1].text(0.1, 0.5, stats_text, fontsize=11, 
                       verticalalignment='center', family='monospace',
                       bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        axes[1, 1].axis('off')
        axes[1, 1].set_title('Summary Statistics', fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        logger.info("Key insights visualization generated successfully")
        
        return fig
        
    except Exception as e:
        logger.error(f"Error creating key insights visualization: {e}")
        raise


def plot_top_products(df, n=20, figsize=(10, 8)):
    """
    Create a horizontal bar chart of top N products.
    
    Args:
        df (pd.DataFrame): Dataframe with product_name column
        n (int): Number of top products to display (default: 20)
        figsize (tuple): Figure size (default: (10, 8))
        
    Returns:
        matplotlib.figure.Figure: Figure object
    """
    try:
        top_products = df['product_name'].value_counts().head(n)
        
        fig, ax = plt.subplots(figsize=figsize)
        ax.barh(range(len(top_products)), top_products.values, color='steelblue')
        ax.set_yticks(range(len(top_products)))
        ax.set_yticklabels(top_products.index)
        ax.set_xlabel('Number of Purchases')
        ax.set_title(f'Top {n} Most Purchased Products', fontsize=14, fontweight='bold')
        ax.invert_yaxis()
        
        # Add value labels
        for i, v in enumerate(top_products.values):
            ax.text(v + 0.5, i, str(v), va='center')
        
        plt.tight_layout()
        logger.info(f"Top {n} products plot created")
        
        return fig
        
    except Exception as e:
        logger.error(f"Error creating top products plot: {e}")
        raise


def plot_order_distribution(df, figsize=(10, 6)):
    """
    Create a histogram showing the distribution of products per order.
    
    Args:
        df (pd.DataFrame): Dataframe with order_id column
        figsize (tuple): Figure size (default: (10, 6))
        
    Returns:
        matplotlib.figure.Figure: Figure object
    """
    try:
        products_per_order = df.groupby('order_id').size()
        
        fig, ax = plt.subplots(figsize=figsize)
        ax.hist(products_per_order, bins=30, color='coral', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Number of Products per Order')
        ax.set_ylabel('Frequency')
        ax.set_title('Distribution of Products per Order', fontsize=14, fontweight='bold')
        
        # Add mean and median lines
        ax.axvline(products_per_order.mean(), color='red', linestyle='--', 
                   linewidth=2, label=f'Mean: {products_per_order.mean():.1f}')
        ax.axvline(products_per_order.median(), color='green', linestyle='--', 
                   linewidth=2, label=f'Median: {products_per_order.median():.1f}')
        ax.legend()
        
        plt.tight_layout()
        logger.info("Order distribution plot created")
        
        return fig
        
    except Exception as e:
        logger.error(f"Error creating order distribution plot: {e}")
        raise


def plot_heatmap(matrix, figsize=(12, 10), top_n=50):
    """
    Create a heatmap visualization of product co-occurrence.
    
    Args:
        matrix (pd.DataFrame): Binary transaction matrix
        figsize (tuple): Figure size (default: (12, 10))
        top_n (int): Number of top products to include (default: 50)
        
    Returns:
        matplotlib.figure.Figure: Figure object
    """
    try:
        # Get top N products by frequency
        product_freq = matrix.sum(axis=0).sort_values(ascending=False).head(top_n)
        top_products = product_freq.index
        
        # Filter matrix to top products
        filtered_matrix = matrix[top_products]
        
        # Calculate co-occurrence matrix
        co_occurrence = filtered_matrix.T.dot(filtered_matrix)
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(co_occurrence, cmap='YlOrRd', ax=ax, 
                   cbar_kws={'label': 'Co-occurrence Count'})
        ax.set_title(f'Product Co-occurrence Heatmap (Top {top_n} Products)', 
                    fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        logger.info(f"Heatmap created for top {top_n} products")
        
        return fig
        
    except Exception as e:
        logger.error(f"Error creating heatmap: {e}")
        raise


def plot_association_rules(rules_df, metric='lift', figsize=(10, 8)):
    """
    Create a scatter plot of association rules.
    
    Args:
        rules_df (pd.DataFrame): Dataframe containing association rules
        metric (str): Metric to plot on y-axis ('lift', 'confidence', 'support')
        figsize (tuple): Figure size (default: (10, 8))
        
    Returns:
        matplotlib.figure.Figure: Figure object
    """
    try:
        fig, ax = plt.subplots(figsize=figsize)
        
        scatter = ax.scatter(rules_df['support'], rules_df[metric], 
                           c=rules_df['confidence'], cmap='viridis',
                           s=100, alpha=0.6, edgecolors='black')
        
        ax.set_xlabel('Support', fontsize=12)
        ax.set_ylabel(metric.capitalize(), fontsize=12)
        ax.set_title(f'Association Rules: Support vs {metric.capitalize()}', 
                    fontsize=14, fontweight='bold')
        
        # Add colorbar
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Confidence', fontsize=11)
        
        plt.tight_layout()
        logger.info("Association rules plot created")
        
        return fig
        
    except Exception as e:
        logger.error(f"Error creating association rules plot: {e}")
        raise
