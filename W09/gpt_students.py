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
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = row['I-Number']
                value = row['Name']
                student_dict[key] = value
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    return student_dict

def main():
    filename = 'students.csv'
    student_dict = read_dictionary(filename)

    if student_dict:
        print("Student Dictionary:")
        for key, value in student_dict.items():
            print(f"{key}: {value}")
    else:
        print("Error reading the student dictionary.")

if __name__ == "__main__":
    main()
