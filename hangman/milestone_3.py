import random
# while True:
#     guess = input("Please enter a single letter: ")
    
#     if len(guess) == 1 and guess.isalpha():
#         break
#     else:
#         print("Invalid letter. Please, enter a single alphabetical character.")p

word_list = ["orange", "pear", "apple", "pineapple", "pumkin"]
## print(word_list)

word = random.choice(word_list)
## print(word)

guess = input("Please enter a single letter: ")

if guess in word:
  print(f"Good guess! {guess} is in the word.")
else:
  print(f"Sorry, {guess} is not in the word. Try again.")