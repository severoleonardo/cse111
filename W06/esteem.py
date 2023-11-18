# esteem.py

def get_user_response(statement_number, statement):
    response = input(f"{statement_number}. {statement}\n   Enter D, d, a, or A: ").strip().upper()
    while response not in ['D', 'd', 'a', 'A']:
        print("Invalid input. Please enter D, d, a, or A.")
        response = input(f"{statement_number}. {statement}\n   Enter D, d, a, or A: ").strip().upper()
    return response

def compute_score(response, reverse_scoring=False):
    scoring = {'D': 0, 'd': 1, 'a': 2, 'A': 3}
    if reverse_scoring:
        scoring = {k: 3-v for k, v in scoring.items()}
    return scoring[response]

def main():
    statements = [
        "I feel that I am a person of worth, at least on an equal plane with others.",
        "I feel that I have a number of good qualities.",
        "All in all, I am inclined to feel that I am a failure.",
        "I am able to do things as well as most other people.",
        "I feel I do not have much to be proud of.",
        "I take a positive attitude toward myself.",
        "On the whole, I am satisfied with myself.",
        "I wish I could have more respect for myself.",
        "I certainly feel useless at times.",
        "At times I think I am no good at all."
    ]
    
    # Statements 3, 5, 8, 9, and 10 are negatively worded and the scoring is reversed.
    reversed_statements = [2, 4, 7, 8, 9]
    
    total_score = 0
    
    for i, statement in enumerate(statements):
        response = get_user_response(i+1, statement)
        score = compute_score(response, reverse_scoring=(i in reversed_statements))
        total_score += score
    
    print("\nYour score is {}.".format(total_score))
    if total_score < 15:
        print("A score below 15 may indicate problematic low self-esteem.")

if __name__ == "__main__":
    main()
