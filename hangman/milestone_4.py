import random

word_list = ["orange", "pear", "apple", "pineapple", "pumkin"]

class hangman:

    def __init__(self, word_list=["orange", "pear", "apple", "pineapple", "pumkin"], num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


    def check_guess(guess):


        word = random.choice(word_list)
## print(word)
        num_lives = 5
        guess = input("Please enter a single letter: ")
        guess = guess.lower()
        word_guessed = ['_' for _ in word]
        num_letters = len(set(word))

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    word_guessed[i] = guess
            num_letters -= 1
        else:
            num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {num_lives} lives left.")

    def ask_for_input(check_guess):
        list_of_guesses = []
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
                list_of_guesses.append(guess)
                
hangman = hangman(word_list)

# Call the ask_for_input method
hangman.check_guess()