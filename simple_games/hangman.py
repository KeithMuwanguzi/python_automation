import random

def choose_word():
    # List of words to choose from
    words = ["python", "hangman", "programming", "computer", "game", "code", "algorithm"]

    # Choose a random word from the list
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters revealed and others as underscores
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    num_guesses = 7

    while num_guesses > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word_to_guess:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            print("Incorrect!")
            num_guesses -= 1

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

        print("You have", num_guesses, "guesses left.")

    if num_guesses == 0:
        print("\nSorry, you've run out of guesses. The word was:", word_to_guess)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman()
