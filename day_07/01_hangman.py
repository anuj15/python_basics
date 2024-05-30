import random

from hangman_ascii_art import stages, logo
from hangman_words import word_list

# SELECT A RANDOM WORD FROM A LIST OF WORDS
chosen_word = (random.choice(word_list)).lower()
chosen_word_list = [_ for _ in chosen_word]

blank_word = ''
# CREATE ALL BLANKS FOR THE CHOSEN WORD
for i in chosen_word_list:
    blank_word += '_'
blank_word_list = [_ for _ in blank_word]
guessed_words = []
lives = 6

print(f'Welcome to the Hangman Game! Guess the word and save a life.\n{logo}\nInitial Stage: {stages[lives]}')

# Repeat the game till all lives are exhausted or user wins the game.
while lives > 0:

    # ASK USER TO GUESS A LETTER
    guessed_letter = input('Guess a letter: ').lower()

    # If user guesses more than 1 character at a time then ask him to guess again.
    if len(guessed_letter) > 1:
        print('Invalid Input. You need to guess 1 letter at a time.')

    # If user has already guessed this letter then tell him so.
    elif guessed_letter in guessed_words:
        print('This letter is already guessed. Guess again!')

    # IF GUESSED LETTER IS PRESENT IN CHOSEN WORD THEN ADD IT TO BLANK WORD AND CHECK IF WORD IS COMPLETED OR NOT
    #       IF NOT THEN ASK USER TO GUESS AGAIN.
    #       IF YES THEN GAME OVER, USER WON
    elif guessed_letter in chosen_word_list:
        guessed_words.append(guessed_letter)
        for letter in range(len(chosen_word_list)):
            if chosen_word_list[letter] == guessed_letter:
                blank_word_list[letter] = guessed_letter
        if blank_word_list == chosen_word_list:
            print(f'Game Over. You won! The word was: {chosen_word}')
            break

    # IF GUESSED LETTER IS NOT PRESENT IN CHOSEN WORD THEN REMOVE 1 LIFE AND CHECK IF LIVES ARE EXHAUSTED OR NOT
    #       IF NOT THEN ASK USER TO GUESS AGAIN
    #       IF YES THEN GAME OVER, USER LOSE
    else:
        guessed_words.append(guessed_letter)
        lives -= 1

        if lives == 0:
            print(f'Game Over. You lose! The word was: {chosen_word}')
    print(f'Current progress: {"".join(blank_word_list)}')
    print(f'{stages[lives]}\n')
