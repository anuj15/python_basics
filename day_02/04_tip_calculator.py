# Program to calculate tip
print('Welcome to the tip calculator!')
total_amount = float(input('What was the total bill? $'))
tip_percent = int(input('How much tip would you like to give? 10, 12, or 15? '))
head_count = int(input('How many people to split the bill? '))
amount_per_head = round((total_amount + total_amount * tip_percent / 100) / head_count, 2)
print(f'Each person should pay: ${amount_per_head:.2f}'.format())
