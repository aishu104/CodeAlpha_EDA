import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
df = pd.read_csv("books.csv")

# Display data
print(df.head())

# Dataset information
print(df.info())

# Missing values
print(df.isnull().sum())

# Duplicate records
print(df.duplicated().sum())

# Clean Price column
df["Price"] = df["Price"].replace(r"[^0-9.]", "", regex=True)
df["Price"] = pd.to_numeric(df["Price"])

# Convert Rating
rating = {
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
}

df["Rating"] = df["Rating"].map(rating)

# Summary statistics
print(df.describe())

# Price Distribution
plt.hist(df["Price"])
plt.title("Price Distribution")
plt.show()

# Rating Distribution
sns.countplot(x="Rating", data=df)
plt.title("Book Ratings")
plt.show()

# Price vs Rating
sns.scatterplot(x="Rating", y="Price", data=df)
plt.title("Price vs Rating")
plt.show()