import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = {
    "Laptop": 1200,
    "Monitor": 350,
    "Keyboard": 80,
    "Mouse": 40,
    "Headphones": 150,
}

start_date = datetime(2025, 1, 1)

data = []

for _ in range(1000):
    product = random.choice(list(products.keys()))
    quantity = random.randint(1, 5)

    date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    price = products[product]

    revenue = quantity * price

    data.append(
        {
            "date": date.strftime("%Y-%m-%d"),
            "product": product,
            "quantity": quantity,
            "unit_price": price,
            "revenue": revenue,
        }
    )

df = pd.DataFrame(data)

df.to_csv(
    "data/sales_data.csv",
    index=False
)

print("Sales data successfully generated!")
print(df.head())
