# Program to print outcome of a coin toss
import random

options = [0, 1]
toss = random.choice(options)
if toss == 0:
    print('Heads')
else:
    print('Tails')
