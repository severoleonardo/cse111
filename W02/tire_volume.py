'''
Assignment: 02 Prove: Calling Functions
Dev: Leonardo Severo Elias

Pupose: Prove that you can write a Python program that calls functions and methods to get the current date and to append values to a text file.
'''

# Import the math module so I can use math.pi and math.sqrt
import math
import datetime

# Get input from the user for tire specifications
width_mm = float(input("Enter the width of the tire in millimeters: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter_inch = float(input("Enter the diameter of the wheel in inches: "))

# Calculate the volume of space inside the tire
volume_liters = (math.pi * width_mm**2 * aspect_ratio * (width_mm * aspect_ratio + 2540 * diameter_inch)) / 10000000000



# Get the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Open and append to the volumes.txt file
with open("volumes.txt", "at") as volumes:
    # Append a line with current fate, tire specifications, and volume
    volumes.write(f"{current_date}, {int(width_mm)}, {int(aspect_ratio)}, {int(diameter_inch)}, {volume_liters:.2f}\n")


# Print the result
print(f"{current_date}, {int(width_mm)}, {int(aspect_ratio)}, {int(diameter_inch)}, {volume_liters:.2f}\n")