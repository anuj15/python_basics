# Program to calculate remaining weeks of life if life expectancy is 90 years
current_age = int(input('Enter your current age: '))
remaining_years = 90 - current_age
remaining_weeks = remaining_years * 52
print(f'You have {remaining_weeks} weeks left.')
