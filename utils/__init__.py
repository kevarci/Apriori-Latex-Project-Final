"""
Utils package for Apriori Recommendation System.

This package contains utility modules for data loading and visualization.
"""

from .data_loader import (
    load_and_process_data,
    get_transaction_matrix,
    get_top_products,
    get_product_stats,
    prepare_for_apriori
)

from .visualization import (
    plot_key_insights,
    plot_top_products,
    plot_order_distribution,
    plot_heatmap,
    plot_association_rules
)

__all__ = [
    'load_and_process_data',
    'get_transaction_matrix',
    'get_top_products',
    'get_product_stats',
    'prepare_for_apriori',
    'plot_key_insights',
    'plot_top_products',
    'plot_order_distribution',
    'plot_heatmap',
    'plot_association_rules'
]

__version__ = '1.0.0'
