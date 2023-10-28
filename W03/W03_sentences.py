import random

# Main function
def main():
    for _ in range(5): # Generate five sentences
        sentence = make_sentence()
        print(sentence)

# Lists of determiners, nouns and verbs
determiners = ["A", "An", "The", "one", "Some", "Many"] 
nouns = ["cat", "mam", "woman", "girls", "dogs", "men"]
verbs = ["laughed", "eats", "will think", "thought", "run", "will write"]

# Function to get a ramdom determiner
def get_determiner():
    return random.choice(determiners)

# Function to get a ramdom noun
def get_noun():
    return random.choice(nouns)

# Function to get a random verb
def get_verb():
    return random.choice(verbs)

# Function to create a sentence
def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    return f"{determiner} {noun} {verb}."

main()
