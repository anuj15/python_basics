# Program to check if a year is leap year or not
year = int(input('Enter the year: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap Year.')
        else:
            print(f'{year} is not a leap Year.')
    else:
        print(f'{year} is a leap Year.')
else:
    print(f'{year} is not a leap Year.')
