# Program to find maximum from a list
scores = input('Enter comma separated values of score: ').split()
max_score = 0
for score in scores:
    if max_score < int(score):
        max_score = int(score)
print(f'The maximum score is: {max_score}.')
