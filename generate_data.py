import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility (shows you know NumPy's random module)
np.random.seed(42)

# Number of records
num_records = 5000

# Generate realistic dates over 2 years
start_date = datetime(2022, 1, 1)
dates = [start_date + timedelta(days=np.random.randint(0, 730)) for _ in range(num_records)]

# Define product categories and regions
regions = ['West', 'East', 'South', 'Central']
categories = ['Furniture', 'Technology', 'Office Supplies']
products = ['iPhone 14', 'MacBook Pro', 'Desk Chair', 'Paper Set', 'Canon Copier', 
            'Monitor 27"', 'Keyboard', 'Mouse', 'Standing Desk', 'Pen Set']

# Generate the data using NumPy's random choices and arithmetic
df = pd.DataFrame({
    'Order Date': dates,
    'Region': np.random.choice(regions, num_records),
    'Category': np.random.choice(categories, num_records),
    'Product Name': np.random.choice(products, num_records),
    'Sales': np.round(np.random.uniform(15, 600, num_records), 2),  # Uniform distribution
    'Quantity': np.random.randint(1, 8, num_records),
    'Profit': np.round(np.random.normal(20, 30, num_records), 2)    # Normal distribution (some losses)
})

# Sort by date to simulate a real timeline
df.sort_values('Order Date', inplace=True)

# Save to the data folder
df.to_csv('data/sales_data.csv', index=False)

print("✅ Synthetic sales_data.csv successfully generated using NumPy & Pandas!")
print(f"📊 Generated {num_records} records with {df['Region'].nunique()} regions and {df['Category'].nunique()} categories.")