# Program to find average from a list
heights = input('Enter comma separated values of height in centi-meters: ').split()
sum_of_heights = 0
counter = 0
for height in heights:
    sum_of_heights += int(height)
average_height = sum_of_heights // len(heights)
print(f'The average height is: {average_height} cm.')
