# Program to find sum for fist N numbers
target = int(input('Enter a number between 0 and 1000: '))
total = 0
for i in range(2, target + 1, 2):
    total += i
print(total)
