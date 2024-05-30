# Program to check eligibility to ride a rollercoaster
print('Welcome to the rollercoaster!')
bill = 0
photo_price = 3
height = int(input('What is your height in cm? '))
if height >= 120:
    print('You are eligible too ride the rollercoaster.')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print(f'Child tickets are ${bill}.')
    elif age <= 18:
        bill = 7
        print(f'Youth tickets are ${bill}.')
    elif 45 <= age <= 55:
        print('Everything is going to be ok. Have a free ride on us.')
    else:
        bill = 12
        print(f'Adult tickets are ${bill}.')
    wants_photo = input('Do you want a photo taken? Y or N: ')
    if wants_photo == 'Y':
        bill += photo_price
        print(f'Your final bill is: {bill}')
else:
    print('You are not eligible to ride the rollercoaster.')
