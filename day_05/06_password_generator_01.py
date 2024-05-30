import random

print('Welcome to the PyPassword Generator!')
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "9", "8", "0"]
symbols = ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "_", "+", "=", "-"]
password = []
count_of_letters = int(input('How many letters would you like in your password?\n'))
count_of_numbers = int(input('How many numbers would you like?\n'))
count_of_symbols = int(input('How many symbols would you like?\n'))
for letter in range(count_of_letters):
    password.append(random.choice(letters))
for number in range(count_of_numbers):
    password.append(random.choice(numbers))
for symbol in range(count_of_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
print(f'Your password is: {"".join(password)}')
