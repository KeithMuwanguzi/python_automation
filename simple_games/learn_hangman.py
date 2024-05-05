#variables
# - Word to guess
# - list of guessed letters
# - 

import time
import random

def choose_word():
    words = ['cow','Martha',"magic","python", "hangman", "programming", "computer", "game", "code", "algorithm"]
    return random.choice(words)

def display_word(word,guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def in_game():
    guessed_letters = []
    word = choose_word()
    times = 1
    while times <= 7:
        print(f'\nGuessed:  {display_word(word,guessed_letters)}')
        print('\nGuess Letter')
        letter_guess = input('>>>>>>>') 
        if letter_guess in guessed_letters:
            print('\nLetter already guessed, try again')
        elif letter_guess in word:
            guessed_letters.append(letter_guess)
            print('\nCorrect!!')
            print('\nGo ahead and guess another')
        else:
            print('\nIncorrect Guess!!')

            if times != 7:
                print(f'\nYou have {7 - times} more times to guess')
                times += 1
            else:
                print('You have exhausted all your tries')
                print(f'\nThe correct word is:  {word}')
                times += 1
        
        if '_' not in display_word(word,guessed_letters): 
            print(f'\nCongratulations! The correct word guessed is {display_word(word,guessed_letters)}')
            break

    print('\nDo you want to play again? (yes/no):')
    choice = input('>>>')
    if choice.lower() == 'yes' or choice.lower() == 'y':
        in_game()


def play_game():
    print('''
          



Welcome to HangMan Plus, In this game you will be required to guess a word given
to you in the dashes, guessing a letter at a time.
          
Every correct guess pushes you to guess the next letter. Every wrong guess lets you 
try again but with less tries each time, limited to only 7.
          
Start Playing......................Enjoy
          



''')  
    
    time.sleep(3)
    in_game()
    

    
        



if __name__ == "__main__":
    play_game()