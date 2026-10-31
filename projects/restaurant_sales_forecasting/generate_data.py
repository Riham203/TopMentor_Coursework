import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Date range: 1 Year of sales
start_date = datetime(2025, 1, 1)
dates = [start_date + timedelta(minutes=np.random.randint(0, 525600)) for _ in range(5000)]
dates.sort()

# Menu catalog
menu_items = {
    'Truffle Burger': {'category': 'Mains', 'cost': 6.00, 'price': 16.00},
    'Margherita Pizza': {'category': 'Mains', 'cost': 4.00, 'price': 14.00},
    'Caesar Salad': {'category': 'Starters', 'cost': 2.50, 'price': 9.50},
    'Garlic Bread': {'category': 'Starters', 'cost': 1.50, 'price': 6.00},
    'Craft Beer': {'category': 'Beverages', 'cost': 2.00, 'price': 7.00},
    'Iced Tea': {'category': 'Beverages', 'cost': 0.50, 'price': 4.00},
    'Molten Lava Cake': {'category': 'Desserts', 'cost': 3.00, 'price': 8.50},
    'Tiramisu': {'category': 'Desserts', 'cost': 3.50, 'price': 9.00}
}

items_list = list(menu_items.keys())
probabilities = [0.22, 0.20, 0.12, 0.15, 0.12, 0.10, 0.05, 0.04]

data = []
order_id = 1001

for date in dates:
    # 1 to 4 items per order
    num_items = np.random.choice([1, 2, 3, 4], p=[0.3, 0.4, 0.2, 0.1])
    selected_items = np.random.choice(items_list, size=num_items, p=probabilities)
    
    for item in selected_items:
        qty = np.random.choice([1, 2], p=[0.85, 0.15])
        details = menu_items[item]
        data.append({
            'order_id': order_id,
            'timestamp': date,
            'item_name': item,
            'category': details['category'],
            'quantity': qty,
            'cost_price': details['cost'],
            'selling_price': details['price'],
            'order_type': np.random.choice(['Dine-In', 'Takeout', 'Delivery'], p=[0.6, 0.25, 0.15])
        })
    order_id += 1

df = pd.DataFrame(data)
df.to_csv('restaurant_sales.csv', index=False)
print("Dataset 'restaurant_sales.csv' generated successfully with", len(df), "records.")