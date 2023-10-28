# Import the math module so I can use math.pu and math.sqrt
import math

# Print a desciption of this programn for the user to see.
print("This program computes and output the")
print("surface area of a right circular cone.")

# Get the radius and the height from the user.
radius = float(input("Enter the radius of a cone: "))
height = float(input("Enter the height of a cone: "))

# Compute the surface are of the cone. 
radical = math.sqrt(radius**2 + height**2)
surf_area = math.pi * radius * (radius + radical)

# Round the surface area to one digit after the decimal point. 
surf_area = round(surf_area, 1)

# Print the surface area for the user to see. 
print(f"The surface area is {surf_area}")