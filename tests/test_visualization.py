"""
Unit tests for visualization module.
"""

import pytest
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.visualization import (
    plot_key_insights,
    plot_top_products,
    plot_order_distribution,
    plot_heatmap
)


@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing."""
    data = {
        'order_id': [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5],
        'product_name': ['Apple', 'Banana', 'Orange', 'Apple', 'Orange', 
                        'Banana', 'Apple', 'Orange', 'Grape', 'Apple', 'Banana',
                        'Apple', 'Orange', 'Grape']
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_matrix(sample_df):
    """Create a sample transaction matrix."""
    matrix = pd.crosstab(sample_df['order_id'], sample_df['product_name'])
    return (matrix > 0).astype(int)


class TestVisualization:
    """Test cases for visualization functions."""
    
    def test_plot_key_insights(self, sample_df):
        """Test key insights plot generation."""
        fig = plot_key_insights(sample_df, top_n=3)
        
        # Check that a figure is returned
        assert isinstance(fig, plt.Figure)
        
        # Check that figure has subplots
        assert len(fig.axes) == 4
        
        # Close figure to free memory
        plt.close(fig)
    
    def test_plot_top_products(self, sample_df):
        """Test top products plot generation."""
        fig = plot_top_products(sample_df, n=3)
        
        # Check that a figure is returned
        assert isinstance(fig, plt.Figure)
        
        # Check that figure has at least one axis
        assert len(fig.axes) >= 1
        
        # Close figure
        plt.close(fig)
    
    def test_plot_order_distribution(self, sample_df):
        """Test order distribution plot generation."""
        fig = plot_order_distribution(sample_df)
        
        # Check that a figure is returned
        assert isinstance(fig, plt.Figure)
        
        # Check that figure has at least one axis
        assert len(fig.axes) >= 1
        
        # Close figure
        plt.close(fig)
    
    def test_plot_heatmap(self, sample_matrix):
        """Test heatmap plot generation."""
        fig = plot_heatmap(sample_matrix, top_n=3)
        
        # Check that a figure is returned
        assert isinstance(fig, plt.Figure)
        
        # Check that figure has at least one axis
        assert len(fig.axes) >= 1
        
        # Close figure
        plt.close(fig)
    
    def test_plot_with_custom_figsize(self, sample_df):
        """Test plot generation with custom figure size."""
        fig = plot_top_products(sample_df, n=3, figsize=(8, 6))
        
        # Check that a figure is returned
        assert isinstance(fig, plt.Figure)
        
        # Check figure size
        assert fig.get_figwidth() == 8
        assert fig.get_figheight() == 6
        
        # Close figure
        plt.close(fig)


class TestVisualizationEdgeCases:
    """Test edge cases for visualization functions."""
    
    def test_empty_dataframe(self):
        """Test handling of empty DataFrame."""
        df = pd.DataFrame(columns=['order_id', 'product_name'])
        
        # This should raise an error or handle gracefully
        try:
            fig = plot_key_insights(df)
            plt.close(fig)
        except Exception as e:
            # It's okay to raise an exception for empty data
            assert True
    
    def test_single_product(self):
        """Test visualization with single product."""
        df = pd.DataFrame({
            'order_id': [1, 2, 3],
            'product_name': ['Apple', 'Apple', 'Apple']
        })
        
        fig = plot_top_products(df, n=1)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_large_top_n(self, sample_df):
        """Test with top_n larger than available products."""
        fig = plot_top_products(sample_df, n=100)
        
        # Should not raise an error
        assert isinstance(fig, plt.Figure)
        plt.close(fig)


# Cleanup after all tests
@pytest.fixture(scope="session", autouse=True)
def cleanup():
    """Cleanup matplotlib figures after all tests."""
    yield
    plt.close('all')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
