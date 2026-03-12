import pandas as pd
import random
from datetime import datetime, timedelta

products = ["Laptop", "Phone", "Tablet", "Headphones", "Watch", "Shoes", "Jeans", "Shirt"]

categories = {
    "Laptop": "Electronics",
    "Phone": "Electronics",
    "Tablet": "Electronics",
    "Headphones": "Electronics",
    "Watch": "Accessories",
    "Shoes": "Clothing",
    "Jeans": "Clothing",
    "Shirt": "Clothing"
}

regions = ["North", "South", "East", "West"]
payment_methods = ["Credit Card", "UPI", "Debit Card", "Cash"]
delivery_status = ["Delivered", "Pending", "Shipped"]

data = []

start_date = datetime(2023, 1, 1)

for i in range(1000):

    order_id = 10000 + i
    customer_id = random.randint(1000, 2000)

    product = random.choice(products)
    category = categories[product]

    region = random.choice(regions)

    quantity = random.randint(1, 5)
    unit_price = random.randint(50, 1500)

    discount = random.choice([0, 5, 10, 15])

    sales = quantity * unit_price * (1 - discount/100)

    payment = random.choice(payment_methods)

    status = random.choice(delivery_status)

    date = start_date + timedelta(days=random.randint(0, 365))

    data.append([
        order_id,
        customer_id,
        date.strftime("%Y-%m-%d"),
        product,
        category,
        region,
        quantity,
        unit_price,
        discount,
        sales,
        payment,
        status
    ])

df = pd.DataFrame(data, columns=[
    "Order_ID",
    "Customer_ID",
    "Order_Date",
    "Product",
    "Category",
    "Region",
    "Quantity",
    "Unit_Price",
    "Discount (%)",
    "Sales",
    "Payment_Method",
    "Delivery_Status"
])

df.to_csv("sales_data.csv", index=False)

print("Dataset created with industry fields")