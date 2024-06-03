# OUR BLACKJACK HOUSE RULES
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
# Deal both user and computer a starting hand of 2 random card values.
# Detect when computer or user has a blackjack. (Ace + 10 value card).
# If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack,
#   then they win (unless the computer also has a blackjack).
# Calculate the user's and computer's scores based on their card values.
# If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
# Reveal computer's first card to the user.
# Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
# Ask the user if they want to get another card.
# Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep
#   drawing cards unless their score goes over 16.
# Compare user and computer scores and see if it's a win, loss, or draw.
# Print out the player's and computer's final hand and their scores at the end of the game.
# After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.

import random

from blackjack_ascii_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def get_score(player_cards):
    score = 0
    for card in player_cards:
        score += card
    return score


def is_blackjack(player1, player2):
    if get_score(player1) == 21:
        print('Blackjack! You won.')
        return True
    elif get_score(player2) == 21:
        print('Blackjack! You lose.')
        return True
    elif get_score(player1) == 21 and get_score(player2) == 21:
        if len(player1) > len(player2):
            print('Blackjack! You won.')
        elif len(player1) < len(player2):
            print('Blackjack! You lose.')
        else:
            print('It\'s a Draw!')
        return True
    else:
        return False


def print_final_score():
    print(f'Your final hand: {user_cards}, final score: {get_score(user_cards)}')
    print(f'Computer final hand: {computer_cards}, final score: {get_score(computer_cards)}\n')


def print_initial_score():
    print(f'Your cards: {user_cards}, current score: {get_score(user_cards)}')
    print(f'Computer\'s first card: {computer_cards[0]}\n')


def find_winner():
    if not is_blackjack(user_cards, computer_cards):
        if get_score(user_cards) > 21 and 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
            find_winner()
        elif get_score(computer_cards) > 21 and 11 in computer_cards:
            computer_cards.remove(11)
            computer_cards.append(1)
            find_winner()
        elif get_score(user_cards) > 21:
            print_final_score()
            print('You lose.')
        elif get_score(computer_cards) > 21:
            print_final_score()
            print('You won.')
        elif get_score(user_cards) < get_score(computer_cards):
            print_final_score()
            print('You lose.')
        elif get_score(user_cards) > get_score(computer_cards):
            print_final_score()
            print('You won.')
        else:
            print_final_score()
            print('Draw')
    start_game()


def add_card():
    another_card = input('Type \'y\' to get another card, type \'n\' to pass: ')
    if another_card == 'n':
        while get_score(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
        find_winner()
    elif another_card == 'y':
        user_cards.append(random.choice(cards))
        print_initial_score()
        if get_score(user_cards) >= 21 or get_score(computer_cards) >= 21:
            find_winner()
        else:
            add_card()
    else:
        print('Invalid Input. Try again!')
        add_card()


def reset_board():
    user_cards.clear()
    computer_cards.clear()


def start_game():
    play_game = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\' ').lower()

    if play_game == 'y':
        reset_board()
        print(logo)
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        print_initial_score()
        if not is_blackjack(user_cards, computer_cards) or not get_score(user_cards) > 21 or not get_score(
                computer_cards) > 21:
            add_card()
    else:
        return


start_game()
