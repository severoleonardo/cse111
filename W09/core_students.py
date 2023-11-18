import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {}

    try:
        # Open the CSV file for reading
        with open(filename, newline='') as csvfile:
            # Use DictReader to read the CSV file with headers
            reader = csv.DictReader(csvfile)

            # Iterate through each row in the CSV file
            for row in reader:
                # Extract I-Number and Name from each row
                key = row['I-Number']
                value = row['Name']

                # Store the I-Number and Name in the dictionary
                student_dict[key] = value
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    return student_dict

def remove_dashes(i_number):
    """Remove dashes from the given I-Number."""
    return i_number.replace("-", "")

def is_valid_i_number(i_number):
    """Check if the given I-Number is valid."""
    if not i_number.isdigit():
        print("Invalid I-Number")
        return False
    if len(i_number) < 9:
        print("Invalid I-Number: too few digits")
        return False
    if len(i_number) > 9:
        print("Invalid I-Number: too many digits")
        return False
    return True

def main():
    filename = 'students.csv'

    # Read the CSV file into a dictionary
    student_dict = read_dictionary(filename)

    if student_dict:
        # Prompt the user to enter an I-Number
        i_number = input("Enter an I-Number: ")

        # Remove dashes from the entered I-Number
        i_number = remove_dashes(i_number)

        # Check if the I-Number is valid
        if is_valid_i_number(i_number):
            # Check if the entered I-Number is in the dictionary
            if i_number in student_dict:
                # Print the corresponding student name
                print(f"Student Name: {student_dict[i_number]}")
            else:
                # Print a message if the I-Number is not found
                print("No such student.")
        else:
            # Print a message if the I-Number is invalid
            print("Invalid I-Number")
    else:
        print("Error reading the student dictionary.")

if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()
