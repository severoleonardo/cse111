import csv
from datetime import datetime

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

def apply_discount(price, discount_percentage):
    return price * (1 - discount_percentage)

def print_receipt(products_dict, request_file):
    print("\nMy Grocery Store")

    ordered_items = []
    total_items = 0
    subtotal_due = 0

    try:
        # Get the current day of the week
        current_day = datetime.now().strftime("%A")

        # Read and process each row from the request.csv file.
        for row in csv.reader(request_file):
            product_number = row[0]
            quantity = int(row[1])

            # Use the requested product number to find the corresponding item in the products_dict.
            product_info = products_dict[product_number]  # Remove the check for existence

            product_name = product_info[1]
            price = float(product_info[2])

            # Apply discount on Tuesdays and Wednesdays
            if current_day in ['Tuesday', 'Wednesday']:
                price = apply_discount(price, 0.10)

            total_items += quantity
            subtotal_due += quantity * price
            ordered_items.append(f"{product_name}: {quantity} @ ${price:.2f}")

        # Print the list of ordered items.
        print()
        print("\n".join(ordered_items))

        # Print the number of ordered items.
        print(f"\nNumber of Items: {total_items}")

        # Print the subtotal due.
        print(f"Subtotal: ${subtotal_due:.2f}")

        # Compute and print the sales tax amount (6% sales tax rate).
        sales_tax_rate = 0.06
        sales_tax_amount = subtotal_due * sales_tax_rate
        print(f"Sales Tax: ${sales_tax_amount:.2f}")

        # Compute and print the total amount due.
        total_due = subtotal_due + sales_tax_amount
        print(f"Total: ${total_due:.2f}")

        # Print a thank you message.
        print("\nThank you for shopping at My Grocery Store.")

        # Get the current date and time from the computer's operating system.
        current_datetime = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        print(current_datetime)

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except KeyError as ke:
        print(f"Error: unknown product ID in the request.csv file '{ke.args[0]}'")

def main():
    try:
        # Call the read_dictionary function and store the compound dictionary in products_dict.
        products_dict = read_dictionary('products.csv', key_column_index=0)

        # Open the request.csv file for reading.
        with open('request.csv', 'r') as request_file:
            # Skip the first line of the request.csv file because it contains column headings.
            next(request_file)

            # Call the print_receipt function to finish printing the receipt.
            print_receipt(products_dict, request_file)

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")

if __name__ == "__main__":
    main()
