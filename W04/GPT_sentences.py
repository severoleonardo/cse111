import random

# Lists of words
determiners = ["A", "An", "The", "One", "Some", "Many"]
nouns = ["cat", "man", "woman", "girls", "dogs", "men"]
verbs = ["laughed", "eats", "will think", "thought", "run", "will write"]
prepositions = [
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"
]

# Function to get a random determiner
def get_determiner(capitalize_first=True):
    determiner = random.choice(determiners)
    if capitalize_first:
        determiner = determiner.capitalize()
    else:
        determiner = determiner.lower()
    return determiner

# Function to get a random noun
def get_noun():
    return random.choice(nouns)

# Function to get a random verb
def get_verb():
    return random.choice(verbs)

# Function to get a random preposition
def get_preposition():
    return random.choice(prepositions)

# Function to create a prepositional phrase
def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(capitalize_first=False)
    noun = get_noun()
    return f"{preposition} {determiner} {noun}"

# Function to create a sentence with four parts
def make_sentence(quantity, tense):
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    
    # Capitalize the first letter of the sentence and leave the rest in lowercase
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase1} {prepositional_phrase2}."
    return sentence

# Main function
def main():
    characteristics = [(1, "past"), (1, "present"), (1, "future"), (2, "past"), (2, "present"), (2, "future")]

    for quantity, tense in characteristics:
        sentence = make_sentence(quantity, tense)
        print(sentence)


main()