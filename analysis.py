import numpy as np
import pandas as pd

class SalesAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def monthly_revenue(self) -> pd.Series:
        # Use 'ME' instead of 'M' (new pandas offset)
        return self.df.groupby(pd.Grouper(key='Order_Date', freq='ME'))['Sales'].sum()
    
    def top_products(self, n: int = 5) -> pd.Series:
        return self.df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(n)
    
    def regional_sales(self) -> pd.Series:
        return self.df.groupby('Region')['Sales'].sum()
    
    def print_summary_stats(self):
        print("\n" + "="*40)
        print("📊 SALES INSIGHTS (Powered by NumPy & Pandas)")
        print("="*40)
        print(f"Total Revenue: ")
        print(f"Average Order Value: ")
        
        # Using NumPy's percentile
        top_cutoff = np.percentile(self.df['Sales'], 90)
        print(f"Top 10% of orders are above: ")
        
        # Using Pandas date extraction
        self.df['Month'] = self.df['Order_Date'].dt.month_name()
        best_month = self.df.groupby('Month')['Sales'].sum().idxmax()
        print(f"🏆 Best Performing Month: {best_month}")
        print("="*40 + "\n")
