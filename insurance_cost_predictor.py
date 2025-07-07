# insurance_cost_predictor.py

"""
🏥 Insurance Cost Prediction - Linear Regression

Goal:
Predict medical insurance cost based on age, BMI, children, smoking, and region.

Libraries: pandas, sklearn, seaborn, matplotlib

Author: Tejas
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv("insurance.csv")

# Encode categorical features
for col in ['sex', 'smoker', 'region']:
    df[col] = LabelEncoder().fit_transform(df[col])

# Visual: charges vs smoker
sns.boxplot(x='smoker', y='charges', data=df, palette='Set2')
plt.title("🚬 Smoking Impact on Insurance Charges")
plt.xticks([0, 1], ['Non-Smoker', 'Smoker'])
plt.show()

# Prepare features and target
X = df.drop('charges', axis=1)
y = df['charges']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("✅ R² Score:", r2_score(y_test, y_pred))
print("📉 MSE:", mean_squared_error(y_test, y_pred))

# Plot
plt.scatter(y_test, y_pred, alpha=0.5, color='orange')
plt.title("📈 Actual vs Predicted Insurance Charges")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()
