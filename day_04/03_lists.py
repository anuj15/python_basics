# Program to understand lists
import random

names_string = 'Angela, Ben, Chloe, Dan, Elliot'
names = names_string.split(', ')
choice = random.randint(0, len(names) - 1)
print(names[choice])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])
