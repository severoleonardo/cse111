import os

# Get the absolute path to the file
file_path = os.path.abspath("provinces.txt")

# 1. Open the provinces.txt file for reading.
with open(file_path, "r") as file:
    # 2. Read the contents of the file into a list.
    provinces_list = file.read().splitlines()

# 3. Print the entire list.
print("Original List:")
print(provinces_list)

# 4. Remove the first element from the list.
first_element = provinces_list.pop(0)
print(f"\nRemoved First Element: {first_element}")

# 5. Remove the last element from the list.
last_element = provinces_list.pop()
print(f"Removed Last Element: {last_element}")

# 6. Replace all occurrences of "AB" with "Alberta".
provinces_list = [province.replace("AB", "Alberta") for province in provinces_list]

# 7. Count the number of elements that are "Alberta" and print that number.
count_alberta = provinces_list.count("Alberta")
print(f"\nOccurrences of 'Alberta': {count_alberta}")

# Print the modified list.
print("\nModified List:")
print(provinces_list)
