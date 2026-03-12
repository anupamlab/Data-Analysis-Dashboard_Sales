import pandas as pd
import matplotlib.pyplot as plt

# --- Load data ---
data = pd.read_csv("sales_data.csv")

# Convert Order_Date to datetime
data["Order_Date"] = pd.to_datetime(data["Order_Date"])

# --- Show first few rows ---
print("Dataset Preview:")
print(data.head(), "\n")

# --- Key metrics ---
total_sales = data["Sales"].sum()
total_orders = data["Order_ID"].nunique()
total_customers = data["Customer_ID"].nunique()

print("Key Metrics:")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}\n")

# --- Sales by Category ---
category_sales = data.groupby("Category")["Sales"].sum()
print("Sales by Category:")
print(category_sales, "\n")

# Plot Sales by Category
category_sales.plot(kind="bar", title="Sales by Category")
plt.ylabel("Sales")
plt.xlabel("Category")
plt.show()

# --- Sales by Region ---
region_sales = data.groupby("Region")["Sales"].sum()
print("Sales by Region:")
print(region_sales, "\n")

# Plot Sales by Region
region_sales.plot(kind="pie", autopct="%1.1f%%", title="Sales by Region")
plt.ylabel("")
plt.show()

# --- Monthly Sales Trend ---
monthly_sales = data.groupby(data["Order_Date"].dt.month)["Sales"].sum()
print("Monthly Sales Trend:")
print(monthly_sales, "\n")

# Plot Monthly Sales Trend
monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# --- Top 10 Selling Products ---
top_products = data.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)
print("Top 10 Selling Products:")
print(top_products)