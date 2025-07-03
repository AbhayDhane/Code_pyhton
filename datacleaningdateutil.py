import pandas as pd
from dateutil import parser

# 🔹 Create a sample dataset with messy date strings
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'JoinDate': [
        '12/03/2020',      # DD/MM/YYYY
        '15-04-2021',      # DD-MM-YYYY
        'April 15, 2021',  # Month name
        'invalid_date',    # Invalid date
        None               # Missing date
    ]
}

df = pd.DataFrame(data)

# 🔹 Display original DataFrame
print("Original DataFrame:")
print(df)

# 🔹 Define a function that safely parses each date string
def parse_date_safe(date_str):
    """
    Tries to parse a messy date string into a datetime object.
    If parsing fails, returns pd.NaT (missing datetime).
    """
    try:
        # Use dateutil.parser to guess the date format automatically
        return parser.parse(date_str, dayfirst=True, fuzzy=True)
    except (ValueError, TypeError):
        # If parsing fails, return NaT (pandas' missing datetime)
        return pd.NaT

# 🔹 Apply the function to the 'JoinDate' column
df['JoinDate_Clean'] = df['JoinDate'].apply(parse_date_safe)

# 🔹 Display cleaned DataFrame
print("\nCleaned DataFrame with parsed dates:")
print(df)

# 🔹 Optional: Format cleaned dates as DD-MM-YYYY strings
df['JoinDate_Formatted'] = df['JoinDate_Clean'].dt.strftime('%d-%m-%Y')

# 🔹 Display final DataFrame with formatted dates
print("\nDataFrame with formatted dates:")
print(df)
