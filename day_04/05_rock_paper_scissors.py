# Program to simulate rock paper scissor game
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print('Welcome to the ROCK PAPER SCISSORS GAME!')
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))
computer = random.randint(0, 2)
choices = [rock, paper, scissor]
if user < len(choices):
    print(f'You chose:\n{choices[user]}')
    print(f'Computer chose:\n{choices[computer]}')
    if user == computer:
        print('Draw!')
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print('You won!')
    else:
        print('You lose!')
else:
    print('You typed an invalid number. You lose!')
