import csv

def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
    - filename: the name of the CSV file to read.
    - key_column_index: the index of the column
        to use as the keys in the dictionary.

    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    data_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            values = row
            data_dict[key] = values
    return data_dict

def main():
    # Step 4a: Call the read_dictionary function and store the compound dictionary in products_dict.
    products_dict = read_dictionary('products.csv', key_column_index=0)

    # Step 4b: Print the products_dict.
    print("===== All Products =====")
    for key, value in products_dict.items():
        print(f"{key}: {value}")

    # Step 4c: Open the request.csv file for reading.
    with open('request.csv', 'r') as request_file:
        # Step 4d: Skip the first line of the request.csv file because it contains column headings.
        next(request_file)
        print("===== Requested Items =====")
        # Step 4e: Use a loop that reads and processes each row from the request.csv file.
        for row in csv.reader(request_file):
            # Step 4e(i): Use the requested product number to find the corresponding item in the products_dict.
            product_number = row[0]
            product_info = products_dict.get(product_number)

            # Step 4e(ii): Print the product name, requested quantity, and product price.
            
            if product_info:
                product_name = product_info[1]
                quantity = int(row[1])
                print(f"Product: {product_name}, Quantity: {quantity}, Price: {product_info[2]}")

if __name__ == "__main__":
    main()
