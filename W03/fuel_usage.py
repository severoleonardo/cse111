# Define the miles per gallon function
def miles_per_gallon(start, end, gallons):
    mpg = (end - start) / gallons
    return mpg

# Define the liters per 100 kilometers function
def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

# Main function to get user input and display results
def main():
    # Get user input for starting odometer value, ending odometer value, and fuel amount
    start = float(input("Enter the starting odometer value in miles: "))
    end = float(input("Enter the ending odometer value in miles: "))
    gallons = float(input("Enter the amount of fuel in gallons: "))

    # Calculate miles per gallon
    mpg = miles_per_gallon(start, end, gallons)

    # Calculate liters per 100 kilometers using the conversion function
    lp100k = lp100k_from_mpg(mpg)

    # Display the results
    print(f"Fuel efficiency in miles per gallon: {mpg:.2f} mpg")
    print(f"Fuel efficiency in liters per 100 kilometers: {lp100k:.2f} lp100k")

# Call the main function to start the program
if __name__ == "__main__":
    main()
