# Program to find love compatibility
print('LOVE CALCULATOR')
first_name = input('Enter first person\'s name: ').lower()
second_name = input('Enter second person\'s name: ').lower()
names_combined = first_name + second_name
first_digit = 0
second_digit = 0
checker_1 = 'true'
for i in names_combined:
    if i in checker_1:
        first_digit += 1
checker_2 = 'love'
for i in names_combined:
    if i in checker_2:
        second_digit += 1
score = first_digit * 10 + second_digit
if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 < score < 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
