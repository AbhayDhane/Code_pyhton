import pandas as pd  # Importing the pandas library

# Step 1: Create a simple dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Mumbai', 'Delhi', 'Bangalore']
}

# Step 2: Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Display the DataFrame
print("Original DataFrame:")
print(df)

# Step 4: Access a specific column (e.g., Age)
print("\nAges of all people:")
print(df['Age'])

# Step 5: Filter rows where Age is greater than 28
print("\nPeople older than 28:")
print(df[df['Age'] > 28])

# Step 6: Add a new column 'Salary'
df['Salary'] = [50000, 60000, 70000]

# Step 7: Display the updated DataFrame
print("\nUpdated DataFrame with Salary:")
print(df)
