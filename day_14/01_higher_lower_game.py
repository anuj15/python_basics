import random

from game_data import data
from higher_lower_ascii_art import logo, vs


def print_data(data_):
    return f'{data_["name"]}, a {data_["description"]}, from {data_["country"]} with follower count = {data_["follower_count"]}'


def check_winner(data_1, data_2):
    if data_1['follower_count'] > data_2['follower_count']:
        return ['a', data_2]
    else:
        return ['b', data_1]


def start_game():
    score = 0
    print(logo)
    continue_game = True
    data_a = random.choice(data)

    while continue_game:
        print(f'Compare A: {print_data(data_a)}.')
        print(vs)
        data_b = random.choice(data)
        while data_b == data_a:
            data_b = random.choice(data)
        print(f'Against B: {print_data(data_b)}.')
        expected_winner = input('Who has more followers? Type \'A\' or \'B\': ').lower()
        winner = check_winner(data_a, data_b)
        if winner[0] == expected_winner:
            data_a = winner[1]
            score += 1
            print(f'You are right! Current Score: {score}\n\n{"-" * 75}\n\n')
        else:
            print(f'Sorry, that\'s wrong. Final score: {score}')
            continue_game = False


start_game()
