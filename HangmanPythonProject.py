import random
import string
from wordsfile import words

def get_valid_word(words):
    secret_word = random.choice(words) # for choosing a random word from the list
   
    while '-' in words or ' ' in words:
        secret_word = random.choice(words)

    return secret_word.upper()

def hangman():
    secret_word = get_valid_word(words)
    word_letters = set(secret_word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # shows letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', {lives}, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # show current word (e.g , W - R D)
        current_word = [letter if letter in used_letters else '-' for letter in words]
        print('Current word: ', ' '.join(current_word))

        #asking for user for a guess
        user_letter = input("Guess a letter: ").upper()

        # check if valid and not used before
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # takes away a life if wrong
                print('Letter is not in word.')

        # Already guessed
        elif user_letter in used_letters:
            print("You have already used that character. Please try again!")
        
        # Invalid input
        else:
            print("Invalid character. Please try again!!")


   # If the loop ends, either user guessed all letters or ran out of lives
    if lives == 0:
        print('You died, sorry.. The word was: ', secret_word)
    else:   
        print('Congrats! you guessed the word', secret_word, '!!!!')


# Actually call the game function
hangman()





# print("Welcome to Hangman Game!")
# print("You have to guess the word in 6 attempts")  
# print("Hint: It is a programming language")
# print("Good Luck!")
# print("Let's play Hangman!")