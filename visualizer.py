import matplotlib.pyplot as plt
import pandas as pd

def create_dashboard(monthly_revenue, top_products, regional_sales, save_path):
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle('Executive Sales Dashboard', fontsize=20, fontweight='bold')
    
    # 1. Monthly Revenue Trend
    monthly_revenue.plot(ax=axes[0, 0], color='#1f77b4', marker='o')
    axes[0, 0].set_title('Monthly Revenue Trend', fontsize=14)
    axes[0, 0].set_ylabel('Revenue ($)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Top Products
    top_products.plot(kind='barh', ax=axes[0, 1], color='#2ca02c')
    axes[0, 1].set_title('Top 5 Products by Revenue', fontsize=14)
    axes[0, 1].set_xlabel('Total Sales ($)')
    
    # 3. Distribution of Sales (Histogram)
    axes[1, 0].hist(monthly_revenue, bins=15, color='#ff7f0e', edgecolor='black')
    axes[1, 0].set_title('Distribution of Monthly Revenue', fontsize=14)
    axes[1, 0].set_xlabel('Revenue ($)')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Regional Sales (Pie Chart)
    regional_sales.plot(kind='pie', ax=axes[1, 1], autopct='%1.1f%%', startangle=90, colors=['#d62728', '#9467bd', '#8c564b', '#e377c2'])
    axes[1, 1].set_title('Revenue by Region', fontsize=14)
    axes[1, 1].set_ylabel('')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()  # Closes the plot to free memory
    print(f"✅ Dashboard saved to {save_path}")