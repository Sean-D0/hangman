# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

---
## Table of Contents

> ## [Project Description](#project-description)
> ## [Installation Instructions](#installation-instructions)
> ## [Usage Instructions](#usage-instructions)
> ## [Structure of Hangman](#file-structure-of-the-project)
> ## [Testing](#testing)
 
# Project Description

This project takes in a users input (guess) and through the use of python code, compairs the input to a randomly selected word from a known list of words. If all the letters in the choosen word are guessed then the users wins. If the user is unsuccesful with their guess they lose a life. The game runs untill the users is out of lives for has successfully guess the word randomly selected from the list.

The Hangman game uses several key features of Python:

1. **Classes**: The game logic is encapsulated in a class named `hangman`. This allows for better organization and reusability of the code.

2. **Methods**: The `hangman` class contains several methods (`__init__`, `check_guess`, `ask_for_input`, `play_game`) that perform specific tasks related to the game.

3. **Variables**: Various variables are used to keep track of the state of the game, such as `word`, `word_guessed`, `num_letters`, `num_lives`, `word_list`, and `list_of_guesses`.

4. **Loops**: Loops are used in the `ask_for_input` method to repeatedly ask the user for their guess until a valid guess is entered.

5. **Conditionals**: Conditionals are used in the `check_guess` and `ask_for_input` methods to handle different scenarios based on the user's input.

6. **Lists**: Lists are used to store the word to be guessed (`word`), the current state of the word being guessed (`word_guessed`), and the letters that have been guessed (`list_of_guesses`).

7. **Random Module**: The `random` module is used to select a random word from the `word_list` at the start of the game.

8. **Input Function**: The `input` function is used to get the user's guess.

9. **Print Statements**: Print statements are used to display messages to the user, such as whether their guess was correct or incorrect, and whether they won or lost the game.

**Learned Outcome**: This project reinforced my understanding of logical code operations. Breaking down the game into small specific functions allows for the game logic to be followed easily, while making it clear where the code breaks down. For instance, my biggest error while coding this project was the improper use of the "self" argument. Where I wasn't referring back to the `__init__` conditions and was instead creating new variables and calling them, which caused problems within the code.

# Installation Instructions

To install and run this Hangman game, follow these steps:

**Clone the repository**: You can clone the repository to your local machine using Git. If you don't have Git installed, you can download it from the official website. Once Git is installed, open a terminal window and navigate to the directory where you want to clone the repository. Then, run the following command:

    git clone https://github.com/Sean-D0/hangman.git

**How to deploy locally**: 
1. Log on to [GitHub](https://github.com/), click the repository named [hangman](https://github.com/Sean-D0/hangman).
2. Select the dropdown tab "code" and choose Download ZIP.
3. Un-zip files and it's ready to use on your local environment.

## Usage instructions
Once you've successfully installed and started the Hangman game, you can begin playing by following these steps:

1. **Start the game**: When you run the game, you'll see a message welcoming you to Hangman and asking you to guess a letter.

2. **Enter your guess**: Type a single letter that you think is in the word and press Enter. Remember, the game is case-insensitive, so 'a' and 'A' are considered the same.

3. **Check your guess**: If your guess is correct, the game will tell you so and reveal the positions of your guess in the word. If your guess is incorrect, the game will tell you so and subtract a life from your total.

4. **Continue guessing**: Keep guessing letters until you either guess the entire word (in which case you win!) or run out of lives (in which case you lose).

5. **Restart the game**: Once the game is over, you can restart it by running the script again.

Remember, the goal of the game is to guess the word before you run out of lives. Good luck!

## File structure of the project

The file structure is broken down into a series of task through milestone_1.py to milestone_4.py; building up the foundation and logic of the hangman game. With the complete project contained in milestone_5.py, with accompanying comments on the specific reason for each function. All files are contained with the overaching "hangman" folder this includes the README.md document that explains this project.

## Testing

To test the game logic and user experience I ran the game using a selection of inputs. 
Here are the tabled results, with the *Input* being my manually guess enter through the terminal, and the *output* being the result based on the code logic. 

> Choosen Word: pear

| Input :   |         1 |
| -------- | -------- |
| Output :  | Invalid letter. Please, enter a single alphabetical character.

| Input :   |         aa |
| -------- | -------- |
| Output :  | Invalid letter. Please, enter a single alphabetical character.

| Input :   |         Q |
| -------- | -------- |
| Output :  | Sorry, q is not in the word. Try again. You have 4 lives left.

| Input :   |      p    |
| -------- | -------- |
| Output :  | Good guess! p is in the word.

| Input :   |      a    |
| -------- | -------- |
| Output :  | Good guess! a is in the word.

| Input :   |      r    |
| -------- | -------- |
| Output :  | Good guess! r is in the word.

| Input :   |      e    |
| -------- | -------- |
| Output :  | Good guess! e is in the word. Congratulations. You won the game!

>Choosen word: pumkin

| Input :   |      o    |
| -------- | -------- |
| Output :  | Sorry, o is not in the word. Try again. You have 4 lives left.

| Input :   |      t    |
| -------- | -------- |
| Output :  | Sorry, t is not in the word. Try again. You have 3 lives left.

| Input :   |      w    |
| -------- | -------- |
| Output :  | Sorry, w is not in the word. Try again. You have 2 lives left.

| Input :   |      l    |
| -------- | -------- |
| Output :  | Sorry, l is not in the word. Try again. You have 1 lives left.

| Input :   |      h    |
| -------- | -------- |
| Output :  | Sorry, h is not in the word. Try again. You have 0 lives left. You Lost!