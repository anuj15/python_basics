# Swap 2 numbers using 3rd variable
a, b = 2, 3
print(f'Before swapping\na: {a}, b: {b}')
c = a
a = b
b = c
print(f'After swapping\na: {a}, b: {b}')

# Swap 2 numbers without using 3rd variable
a, b = 2, 3
print(f'Before swapping\na: {a}, b: {b}')
a = a + b
b = a - b
a = a - b
print(f'After swapping\na: {a}, b: {b}')

# Swap 2 numbers in a single line
a, b = 2, 3
print(f'Before swapping\na: {a}, b: {b}')
a, b = b, a
print(f'After swapping\na: {a}, b: {b}')
