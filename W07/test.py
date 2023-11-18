
# # Loop through a collection
# for name in ['Leonardo', 'Zara', 'Maísa']:
#     print(name)

# # Looping a number of times 
# for index in range(0, 2):
#     print(index)

# # Looping with a condition
# names = ['Christopher', 'Susan']
# index = 0
# while index < len(names):
#     print(names[index])
#     # Change the condition!!
#     index = index + 1

# # Example 1

# def main():
#     # Create a list that contains five strings.
#     colors = ["yellow", "red", "green", "yellow", "blue"]

#     # Call the built-in len function
#     # and print the length of the list.
#     length = len(colors)
#     print(f"Number of elements: {length}")

#     # Print the element that is stored
#     # at index 2 in the colors list.
#     print(colors[2])

#     # Change the element that is stored at
#     # index 3 from "yellow" to "purple".
#     colors[3] = "purple"

#     # Print the entire colors list.
#     print(colors)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# # Example 2

# def main():
#     # Create an empty list that will hold fabric names.
#     fabrics = []

#     # Add three elements at the end of the fabrics list.
#     fabrics.append("velvet")
#     fabrics.append("denim")
#     fabrics.append("gingham")

#     # Insert an element at the beginning of the fabrics list.
#     fabrics.insert(0, "chiffon")
#     print(fabrics)

#     # Determine if gingham is in the fabrics list.
#     if "gingham" in fabrics:
#         print("gingham is in the list.")
#     else:
#         print("gingham is NOT in the list.")

#     # Get the index where velvet is stored in the fabrics list.
#     i = fabrics.index("velvet")

#     # Replace velvet with taffeta.
#     fabrics[i] = "taffeta"

#     # Remove the last element from the fabrics list.
#     fabrics.pop()

#     # Remove denim from the fabrics list.
#     fabrics.remove("denim")

#     # Get the length of the fabrics list and print it.
#     n = len(fabrics)
#     print(f"The fabrics list contains {n} elements.")
#     print(fabrics)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# # Example 3

# def main():
#     # Create a list of color names.
#     colors = ["red", "orange", "yellow", "green", "blue"]

#     # Use a for loop to print each element in the list.
#     for color in colors:
#         print(color)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# # Example 4

# def main():
#     # Count from zero to nine by one.
#     for i in range(10):
#         print(i)
#     print()

#     # Count from five to nine by one.
#     for i in range(5, 10):
#         print(i)
#     print()

#     # Count from zero to eight by two.
#     for i in range(0, 10, 2):
#         print(i)
#     print()

#     # Count from 100 down to 70 by three.
#     for i in range(100, 69, -3):
#         print(i)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# # Example 5

# def main():
#     # Create a list of color names.
#     colors = ["red", "orange", "yellow", "green", "blue"]

#     # Use a for loop to print each element in the list.
#     for color in colors:
#         print(color)

#     print()

#     # Use a different for loop to
#     # print each element in the list.
#     for i in range(len(colors)):
#         # Use the index i to retrieve
#         # an element from the list.
#         color = colors[i]

#         print(color)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# Example 6

def main():
    sum = 0

    # Get ten or fewer numbers from the user and
    # add them together.
    for i in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number

    # Print the sum of the numbers for the user to see.
    print(f"sum: {sum}")


# Call main to start this program.
if __name__ == "__main__":
    main()