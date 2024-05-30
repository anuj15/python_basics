# Program to order pizza
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_for_small = 2
pepperoni_for_medium_or_large = 3
cheese = 1
final_bill = 0
print('Thank you for choosing Python Pizza Deliveries!')
size = input('What size pizza do you want: S, M, or L: ')
add_pepperoni = input('Do you want pepperoni? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')
if size == 'S':
    final_bill += small_pizza
elif size == 'M':
    final_bill += medium_pizza
else:
    final_bill += large_pizza
if add_pepperoni == 'Y':
    if size == 'S':
        final_bill += 2
    else:
        final_bill += 3
if extra_cheese == 'Y':
    final_bill += cheese
print(f'Your final bill is ${final_bill}.')
