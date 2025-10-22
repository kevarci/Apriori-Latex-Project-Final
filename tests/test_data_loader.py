"""
Unit tests for data_loader module.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.data_loader import (
    load_and_process_data,
    get_transaction_matrix,
    get_top_products,
    get_product_stats,
    prepare_for_apriori
)


@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing."""
    data = {
        'order_id': [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4],
        'product_name': ['Apple', 'Banana', 'Orange', 'Apple', 'Orange', 
                        'Banana', 'Apple', 'Orange', 'Grape', 'Apple', 'Banana']
    }
    return pd.DataFrame(data)


class TestDataLoader:
    """Test cases for data loader functions."""
    
    def test_get_transaction_matrix(self, sample_df):
        """Test transaction matrix creation."""
        matrix = get_transaction_matrix(sample_df)
        
        # Check that it's a DataFrame
        assert isinstance(matrix, pd.DataFrame)
        
        # Check dimensions
        assert matrix.shape[0] == 4  # 4 unique orders
        assert matrix.shape[1] == 4  # 4 unique products
        
        # Check that values are binary
        assert set(matrix.values.flatten()) == {0, 1}
    
    def test_get_top_products(self, sample_df):
        """Test getting top products."""
        top_products = get_top_products(sample_df, n=3)
        
        # Check that it's a Series
        assert isinstance(top_products, pd.Series)
        
        # Check length
        assert len(top_products) <= 3
        
        # Check that it's sorted in descending order
        assert all(top_products.iloc[i] >= top_products.iloc[i+1] 
                  for i in range(len(top_products)-1))
    
    def test_get_product_stats(self, sample_df):
        """Test product statistics calculation."""
        stats = get_product_stats(sample_df)
        
        # Check that it's a dictionary
        assert isinstance(stats, dict)
        
        # Check required keys
        required_keys = ['total_orders', 'total_products', 'total_transactions',
                        'avg_products_per_order', 'median_products_per_order']
        assert all(key in stats for key in required_keys)
        
        # Check values
        assert stats['total_orders'] == 4
        assert stats['total_products'] == 4
        assert stats['total_transactions'] == 11
    
    def test_prepare_for_apriori_list(self, sample_df):
        """Test preparing data for Apriori in list format."""
        transactions = prepare_for_apriori(sample_df, format='list')
        
        # Check that it's a list
        assert isinstance(transactions, list)
        
        # Check that each transaction is a list
        assert all(isinstance(t, list) for t in transactions)
        
        # Check number of transactions
        assert len(transactions) == 4
    
    def test_prepare_for_apriori_matrix(self, sample_df):
        """Test preparing data for Apriori in matrix format."""
        matrix = prepare_for_apriori(sample_df, format='matrix')
        
        # Check that it's a DataFrame
        assert isinstance(matrix, pd.DataFrame)
        
        # Check that values are binary
        assert set(matrix.values.flatten()) == {0, 1}
    
    def test_prepare_for_apriori_invalid_format(self, sample_df):
        """Test that invalid format raises ValueError."""
        with pytest.raises(ValueError):
            prepare_for_apriori(sample_df, format='invalid')


class TestDataLoaderEdgeCases:
    """Test edge cases for data loader functions."""
    
    def test_empty_dataframe(self):
        """Test handling of empty DataFrame."""
        df = pd.DataFrame(columns=['order_id', 'product_name'])
        
        # This should not raise an error
        stats = get_product_stats(df)
        assert stats['total_orders'] == 0
        assert stats['total_products'] == 0
    
    def test_single_order(self):
        """Test handling of single order."""
        df = pd.DataFrame({
            'order_id': [1, 1, 1],
            'product_name': ['Apple', 'Banana', 'Orange']
        })
        
        stats = get_product_stats(df)
        assert stats['total_orders'] == 1
        assert stats['total_products'] == 3
    
    def test_duplicate_products_in_order(self):
        """Test handling of duplicate products in same order."""
        df = pd.DataFrame({
            'order_id': [1, 1, 1],
            'product_name': ['Apple', 'Apple', 'Banana']
        })
        
        matrix = get_transaction_matrix(df)
        # Should treat duplicates as single occurrence
        assert matrix.loc[1, 'Apple'] == 1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
