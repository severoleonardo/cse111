# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def main():
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    # Initialize score
    score = 0

    # Array of tuples, each containing a statement and its type (True for positive, False for negative)
    questions = [
        ("1. I feel that I am a person of worth, at least on an equal plane with others.", True),
        ("2. I feel that I have a number of good qualities.", True),
        ("3. All in all, I am inclined to feel that I am a failure.", False),
        ("4. I am able to do things as well as most other people.", True),
        ("5. I feel I do not have much to be proud of.", False),
        ("6. I take a positive attitude toward myself.", True),
        ("7. On the whole, I am satisfied with myself.", True),
        ("8. I wish I could have more respect for myself.", False),
        ("9. I certainly feel useless at times.", False),
        ("10. At times I think I am no good at all.", False)
    ]

    # Loop through the questions and update the score
    for statement, is_positive in questions:
        if not is_positive:
            score += ask_question(statement, is_positive)
        else:
            score += ask_question(statement, is_positive)

    # Print the final score
    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def ask_question(statement, is_positive):
    """Display a statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        is_positive: True if the statement is positive, False if negative.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("   Enter D, d, a, or A: ").strip().upper()

    # Dictionary mapping user responses to their respective scores
    # Positive questions have a direct mapping, negative ones are reversed
    scores = {'D': 0, 'd': 1, 'a': 2, 'A': 3} if is_positive else {'D': 3, 'd': 2, 'a': 1, 'A': 0}

    # Validate the input and reprompt if necessary
    while answer not in scores:
        print("Invalid input. Please enter D, d, a, or A.")
        answer = input("   Enter D, d, a, or A: ").strip().upper()

    return scores[answer]

# If this file was executed directly, call the main function.
if __name__ == "__main__":
    main()
