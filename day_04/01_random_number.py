# Program to create a random number b/w 0 and 5
import random

rand_float = random.random() * 5  # random.random() gives a number b/w 0 & 1
rand_float = round(rand_float, 1)
print(rand_float)
