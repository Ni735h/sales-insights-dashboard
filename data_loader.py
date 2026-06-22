import pandas as pd
import logging

def load_sales_data(filepath: str) -> pd.DataFrame:
    """Load sales data from a CSV file."""
    try:
        df = pd.read_csv(filepath, encoding='latin-1', parse_dates=['Order Date'])
        df.rename(columns={'Order Date': 'Order_Date'}, inplace=True)
        logging.info(f"✅ Loaded {len(df)} records from {filepath}")
        return df
    except FileNotFoundError:
        logging.error(f"❌ File not found: {filepath}")
        raise