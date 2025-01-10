# Sample data

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write to an Excel file
df.to_excel("output.xlsx", index=False)

print("Data written to output.xlsx")