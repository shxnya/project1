# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
df = pd.read_csv("data.csv", encoding='unicode_escape')

# Preview the data
df.head()
# cleaning the data
df.info()
df.isnull().sum()
# remove missing and wrong data
df = df.dropna(subset=['CustomerID'])
df = df.drop_duplicates()
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
# fix date formats
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# add new column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# exploratory data analysis(EDA)
#top 10 countries by sales
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=country_sales.values, y=country_sales.index)
plt.title('Top 10 Countries by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Country')
plt.show()

#top 10 best selling products
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Quantity Sold')
plt.ylabel('Product')
plt.show()

# sales over time
sales_by_date = df.groupby(df['InvoiceDate'].dt.date)['TotalPrice'].sum()
plt.figure(figsize=(12,6))
sales_by_date.plot()
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

#top customers by spending
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_customers.values, y=top_customers.index)
plt.title('Top 10 Customers by Spending')
plt.xlabel('Total Spent')
plt.ylabel('Customer ID')
plt.show()


