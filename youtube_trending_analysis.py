# youtube_trending_analysis.py

"""
📺 YouTube Trending Video Insights

Goal:
Analyze trending YouTube videos to identify common traits of viral content.

Libraries: pandas, matplotlib, seaborn

Author: Tejas
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("US_youtube_trending_data.csv")

# Convert to datetime
df['trending_date'] = pd.to_datetime(df['trending_date'], errors='coerce')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['publish_hour'] = df['publish_time'].dt.hour

# Most frequent categories
plt.figure(figsize=(10, 5))
df['category'].value_counts().head(10).plot(kind='bar', color='tomato')
plt.title("🎞️ Most Common Video Categories")
plt.ylabel("Video Count")
plt.xticks(rotation=45)
plt.show()

# Engagement: likes vs views
sns.scatterplot(x='views', y='likes', data=df, alpha=0.5)
plt.title("📈 Likes vs Views")
plt.xlabel("Views")
plt.ylabel("Likes")
plt.show()

# Publish hour trends
sns.countplot(x='publish_hour', data=df, palette='Blues')
plt.title("⏰ Publish Time Distribution")
plt.xlabel("Hour")
plt.show()
