import random

from guess_the_number_ascii_art import logo

hard_attempts = 5
easy_attempts = 10


def start_game():
    print(f'Welcome to the Number Guessing Game!\n{logo}')
    print('I\'m thinking of a number between 1 to 100.')
    number = random.randint(1, 100)
    level = choose_difficulty()
    while level > 0:
        user_guess = int(input(f'You have {level} attempts remaining to guess the number. Make a Guess: '))
        if user_guess < number:
            print(f'Too low. Guess again.')
        elif user_guess > number:
            print(f'Too high. Guess again.')
        else:
            print(f'You are right. The number is {number}')
            return
        level -= 1
    if level == 0:
        print('You\'ve run out of guesses. You lose.')


def choose_difficulty():
    level = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()
    if level == 'hard':
        return hard_attempts
    elif level == 'easy':
        return easy_attempts
    else:
        return


start_game()
