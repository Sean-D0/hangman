import random
## List of words used for the game init
word_list = ["orange", "pear", "apple", "pineapple", "pumkin"]
## print(word_list)

word = random.choice(word_list)
## print(word)

## Prompt for user to enter there single character guess
guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else: print("Oops! That is not a valid input.")