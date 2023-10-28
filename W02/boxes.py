'''
Assignment: 02 Checkpoint: Calling Functions
Dev: Leonardo Severo Elias

Pupose: Check your understanding of calling built-in Python functions and functions that are in a standard Python module.

'''
import math

# Get input from user
manufactured_items = int(input("Enter the number of manufactured items: "))
items_per_box = int(input("Enter the number of items to pack per box: "))

# Calculate the number of boxes required
boxes_required = math.ceil(manufactured_items / items_per_box)

# Print the result
print()
print(f"Number of boxes required: {boxes_required}")

