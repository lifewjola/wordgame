# This program generates a random word, then shuffles it, the user will have to unshuffle it to win
import random

# List of words for the game
words = ['dancing', 'tissue', 'christmas', 'melody', 'passover', 'celebration', 'festival', 'decoration', 'lights', 'island', 'treasure', 'savior', 'easter']

# Choose a random word from the list
word = random.choice(words)

# Shuffle the letters of the chosen word
shuffled_word = list(word)
random.shuffle(shuffled_word)

# Convert the shuffled letters back into a string
shuffled_word = ''.join(shuffled_word)

# Print the shuffled word and ask the user to unshuffle it
print(f"Unscramble this word: {shuffled_word}")
guess = input("Your guess: ")

# Check if the user's guess is correct
if guess == word:
    print("You won!")
else:
    print("You lose.")
    print("The word is: ", word)
