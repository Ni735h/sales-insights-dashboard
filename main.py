import argparse
import logging
from data_loader import load_sales_data
from analysis import SalesAnalyzer
from visualizer import create_dashboard

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

def main():
    parser = argparse.ArgumentParser(description="Sales Insights Dashboard")
    parser.add_argument('--file', default='data/sales_data.csv', help='Path to CSV file')
    parser.add_argument('--output', default='dashboard.png', help='Output plot filename')
    args = parser.parse_args()

    # 1. Load data
    df = load_sales_data(args.file)
    
    # 2. Analyze
    analyzer = SalesAnalyzer(df)
    monthly = analyzer.monthly_revenue()
    top_products = analyzer.top_products(5)
    regional_sales = analyzer.regional_sales()

    # Print insights (shows Python & NumPy stats)
    analyzer.print_summary_stats()

    # 3. Visualize
    create_dashboard(monthly, top_products, regional_sales, args.output)

if __name__ == "__main__":
    main()