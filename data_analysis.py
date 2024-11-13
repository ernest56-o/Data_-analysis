import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

# Load Dataset
try:
    data = pd.read_csv("path/to/your/dataset.csv")
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: File not found. Please check the file path and try again.")
    exit()

# Display first few rows
print(data.head())

# Explore the dataset
print("\nData Types:")
print(data.dtypes)

print("\nMissing Values:")
print(data.isnull().sum())

# Clean the dataset (fill missing values)
data = data.fillna(data.mean())
for column in data.select_dtypes(include=["object"]).columns:
    data[column].fillna(data[column].mode()[0], inplace=True)

# Basic Data Analysis
print("\nBasic Statistics:")
print(data.describe())

# Group data by category and calculate mean
grouped_data = data.groupby("Category")["Value"].mean()
print("\nMean value by Category:")
print(grouped_data)

# Visualizations
# 1. Line chart (Sales over time)
plt.figure(figsize=(10, 6))
plt.plot(data["Date"], data["Sales"])
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# 2. Bar chart (Average value by category)
plt.figure(figsize=(8, 6))
grouped_data.plot(kind="bar", color="skyblue")
plt.title("Average Value by Category")
plt.xlabel("Category")
plt.ylabel("Average Value")
plt.show()

# 3. Histogram (Sales distribution)
plt.figure(figsize=(8, 6))
plt.hist(data["Sales"], bins=20, color="lightgreen")
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (Price vs. Quantity)
plt.figure(figsize=(8, 6))
plt.scatter(data["Price"], data["Quantity"], alpha=0.7)
plt.title("Price vs. Quantity")
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.show()
