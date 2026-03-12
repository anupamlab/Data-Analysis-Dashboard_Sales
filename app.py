import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Sales Data Analytics Dashboard")
st.caption("Interactive analysis of sales trends, product performance, and regional revenue "
           "--- Developed by infoanupampal@gmail.com")

# Load dataset
data = pd.read_csv("sales_data.csv")

# Convert date column
data["Order_Date"] = pd.to_datetime(data["Order_Date"])

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(data)

# KPIsst.subheader("Key Metrics")

total_sales = data["Sales"].sum()
total_orders = data["Order_ID"].nunique()
total_customers = data["Customer_ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)

# Sales by Category
st.subheader("Sales by Category")

category_sales = data.groupby("Category")["Sales"].sum()

fig1, ax1 = plt.subplots()
category_sales.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Sales")
ax1.set_xlabel("Category")
st.pyplot(fig1)

# Sales by Region
st.subheader("Sales by Region")

region_sales = data.groupby("Region")["Sales"].sum()

fig2, ax2 = plt.subplots()
region_sales.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")

monthly_sales = data.groupby(data["Order_Date"].dt.month)["Sales"].sum()

fig3, ax3 = plt.subplots()
monthly_sales.plot(kind="line", marker="o", ax=ax3)
ax3.set_xlabel("Month")
ax3.set_ylabel("Sales")
st.pyplot(fig3)

# Top 10 Products
st.subheader("Top 10 Selling Products")

top_products = data.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)

st.dataframe(top_products)