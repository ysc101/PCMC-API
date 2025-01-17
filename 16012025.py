import re

# The input sentence
sentence = "The Transaction ID is ABCD12345 for next payment"

# Regular expression pattern to match the ID
pattern = r"ID is (\w+)"

# Search for the pattern in the sentence
match = re.search(pattern, sentence)

# Extract and print the ID if found
if match:
    transaction_id = match.group(1)
    print("Extracted Transaction ID:", transaction_id)
else:
    print("Transaction ID not found.")


