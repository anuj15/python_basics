# Program to check eligibility to ride a rollercoaster
print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))
if height >= 120:
    print('You are eligible too ride the rollercoaster.')
    age = int(input('What is your age? '))
    if age <= 18:
        print('Please pay $7.')
    else:
        print('Please pay $12.')
else:
    print('You are not eligible to ride the rollercoaster.')
