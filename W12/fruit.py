def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # Reverse and print fruit_list.
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    # Append "orange" to the end of fruit_list and print the list.
    fruit_list.append("orange")
    print(f"appended orange: {fruit_list}")

    # Find where "apple" is located, insert "cherry" before "apple", and print the list.
    apple_index = fruit_list.index("apple")
    fruit_list.insert(apple_index, "cherry")
    print(f"inserted cherry: {fruit_list}")

    # Remove "banana" from fruit_list and print the list.
    fruit_list.remove("banana")
    print(f"removed banana: {fruit_list}")

    # Pop the last element from fruit_list and print the popped element and the list.
    popped_element = fruit_list.pop()
    print(f"popped orange: {fruit_list}")

    # Sort and print fruit_list.
    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    # Clear and print fruit_list.
    fruit_list.clear()
    print(f"cleared: {fruit_list}")

# Call the main function.
if __name__ == "__main__":
    main()
