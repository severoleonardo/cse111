# Import the math module so I can use math.pi and math.sqrt
import math

# Get input from the user for tire specifications
width_mm = float(input("Enter the width of the tire in millimeters: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter_inch = float(input("Enter the diameter of the wheel in inches: "))

# Calculate the volume of space inside the tire
volume_liters = (math.pi * width_mm**2 * aspect_ratio * (width_mm * aspect_ratio + 2540 * diameter_inch)) / 10000000000

# Print the result
print(f"The volume of space inside the tire is approximately {volume_liters:.2f} liters")

