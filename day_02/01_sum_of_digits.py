# Program to find sum of digits of a number
number = input('Enter a number: ')
sum_of_digits = 0
for i in range(len(number)):
    digit = int(number) % 10
    sum_of_digits += digit
    number = int(number) / 10
print(sum_of_digits)
