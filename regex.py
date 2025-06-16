import re  # Import the regex module

# Sample text to search in
text = """
My name is Abhay. You can email me at abhay123@gmail.com or at abhay.dhane@company.co.in.
You can call me at +91-9876543210 or 9876543210.
My birth date is 12/06/2025 and today is 16-06-2025.
"""

# 1️⃣ Pattern to find email addresses
email_pattern = r'[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z.]+'

# 2️⃣ Pattern to find phone numbers (with or without +91-)
phone_pattern = r'(\+91[-\s]?|0)?[6-9]\d{9}'

# 3️⃣ Pattern to find dates (dd/mm/yyyy or dd-mm-yyyy)
date_pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'

# 🔍 Find all emails
emails = re.findall(email_pattern, text)
print("Emails found:", emails)

# 🔍 Find all phone numbers
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", re.findall(r'(\+91[-\s]?\d{10}|\b\d{10}\b)', text))

# 🔍 Find all dates
dates = re.findall(date_pattern, text)
print("Dates found:", dates)
