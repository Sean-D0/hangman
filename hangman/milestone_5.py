## Import random math fucntion to select from word_list.
import random
## word_list use for the game.
word_list = ["orange", "pear", "apple", "pineapple", "pumkin"]
## overal hangman class containing game logic functions.
class hangman:
    ## inital game set up.
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    ## function checking that users guess against word list.
    def check_guess(self, guess):
        guess = guess.lower()
        ## if users guess is in word_list run the code below, and add the guess to word_guessed list.
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        ## if guess isnt in word_list the user losses a life and recieves an outcome message.
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
    ## function prompting user to input a guess.
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            ## checks if guess is not an letter or more than one inputted character.
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            ## logic check to made sure users guess is not a duplicate guess, by checking list_of_guesses.
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            ## adds users guess to list_of_guesses if it is a single letter that has not already been guessed.
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    ## logic to play the game, checks inital conditions of lives and letters within guessed list.         
    def play_game(self, word_list):
         num_lives = 5
         game = hangman(word_list, num_lives)

         while True:
             ## game check if users lives are 0 then game is over.
             if game.num_lives == 0:
                 print("You Lost!")
                 break
             ## checks number of letter guessed against the word from the word_list.
             elif game.num_letters > 0:
                  game.ask_for_input()
            ## if lives remain and all letters are guess in the word randomly choosen from word_list then game is won. 
             else:
                 print("Congratulations. You won the game!")
                 break
## creates and instance of the game, used to check logic and play hangman.           
game = hangman(word_list)
game.play_game(word_list)