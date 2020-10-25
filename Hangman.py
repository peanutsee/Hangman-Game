"""
CREATE A PYTHON HANGMAN GAME
"""

from support import Hangman

word_to_guess = input("Enter word to guess: ").upper()
hangman = Hangman(word_to_guess)


def user_choice(choice):
    if choice == 1:
        return hangman.display_hangman()
    elif choice == 2:
        return hangman.display_guessing_slate()
    elif choice == 3:
        user_guess = input("Enter letter to guess: ").upper()
        return hangman.letter_validator(user_guess)
    else:
        print("INVALID INPUT!!")

print("Welcome to Hangman!!")

# Game Over
not_gameover = True

while not_gameover:
    print('1: Display Hangman\n2: Display Guessing Slate\n3: Enter a letter\n')
    choice = input('Enter your choice: ')
    if choice.isdigit():
        user_choice(int(choice))
    else:
        print("INVALID INPUT!!")
    if ''.join(hangman.guessing_slate) == word_to_guess:
        not_gameover = False
        print("YOU WON!!!")
    elif hangman.error_counter == 10:
        print("YOU LOST!!")


