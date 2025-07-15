
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("vgsales.csv")

# Clean data
df = df.dropna(subset=['Year', 'Global_Sales'])

# Top 10 best-selling games
top_games = df.sort_values(by='Global_Sales', ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x='Name', y='Global_Sales', data=top_games, palette='inferno')
plt.title("🏆 Top 10 Best-Selling Games Globally")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales by platform
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)
platform_sales.plot(kind='bar', color='green')
plt.title("🎮 Global Sales by Platform")
plt.ylabel("Sales (Millions)")
plt.show()

# Genre-wise analysis
sns.boxplot(x='Genre', y='Global_Sales', data=df)
plt.title("📦 Sales Distribution by Genre")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
