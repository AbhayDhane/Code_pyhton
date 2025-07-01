import pandas as pd

# Load the CSV
df = pd.read_csv("employees.csv")

# Preview the dataset
print("Initial data:")
print(df)

# Basic info
print("\nData types and non-null counts:")
print(df.info())

print("\nSummary statistics:")
print(df.describe(include='all'))

# Identify missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Replace missing Name with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')

# Replace missing Age with mean age
mean_age = df.loc[df['Age'].notnull() & (df['Age'] > 0), 'Age'].mean()
df['Age'] = df['Age'].replace('-', pd.NA)  # Replace dash with NaN
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'] = df['Age'].fillna(mean_age)

# Convert JoinDate to datetime, handling multiple formats
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce', dayfirst=True)

# Salary as numeric, fixing negatives
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Fix negative ages
df['Age'] = df['Age'].abs()

# Replace negative salaries with absolute value
df['Salary'] = df['Salary'].abs()

# Find duplicates
duplicates = df.duplicated(subset=['Name', 'Age', 'Department'], keep='first')
print(f"\nDuplicate rows:\n{df[duplicates]}")

# Drop them
df = df.drop_duplicates(subset=['Name', 'Age', 'Department'], keep='first')

# Define salary limits
salary_upper_limit = df['Salary'].mean() + 3 * df['Salary'].std()

# Cap salaries above upper limit
df.loc[df['Salary'] > salary_upper_limit, 'Salary'] = salary_upper_limit

# Normalize Name capitalization
df['Name'] = df['Name'].str.title().str.strip()

# Standardize Department names (e.g., remove accidental spaces)
df['Department'] = df['Department'].str.strip().str.capitalize()

print("\nCleaned data:")
print(df)

# Save to new CSV
df.to_csv("employees_cleaned.csv", index=False)
