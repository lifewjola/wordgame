import random

# Read the list of words from a file
with open('wordbank.txt') as wordbank:
    words = wordbank.read().splitlines()

# Choose a random word from the list
word = random.choice(words)

# Shuffle the letters of the chosen word
shuffled_word = list(word)
random.shuffle(shuffled_word)

# Convert the shuffled letters back into a string
shuffled_word = ''.join(shuffled_word)

# Print the shuffled word and ask the user to unshuffle it
print("Unscramble this word", shuffled_word)
guess = input("Your guess: ")

# Check if the user's guess is correct
if guess == word:
    print("You won!")
else:
    hint = input("Would you like a hint? (yes/no): ")
    if hint.lower() == "yes":
        print("HINT: First letter is ", word[0])
        guess = input("Try again: ")
        if guess == word:
            print("You won!")
        else:
            print("Game over.")
            print("The original word is: ", word)
    elif hint.lower() == "no":
        guess = input("Try again: ")
        if guess == word:
            print("You won!")
        else:
            print("Game over.")
            print("The original word is: ", word)
    else:
        print("Invalid input. Game over")

