# FileNotFoundError
try:
    with open('abc.txt', 'r') as f:
        f.read()
except FileNotFoundError as e:
    print(e)

# KeyError
try:
    a_dict = {'key': 'value'}
    x = a_dict['non_existent_key']
except KeyError as e:
    print(f'Key {e} not found')

# IndexNotFound
try:
    a_list = [1, 2, 3]
    x = a_list[5]
except IndexError as e:
    print(e)

# TypeError
try:
    a_text = 'abc'
    x = a_text + 5
except TypeError as e:
    print(e)

# FileNotFoundError
try:
    with open('abc.txt', 'w') as f:
        print('Inside try block')
except FileNotFoundError as e:
    print('Inside except block')
else:
    print('Inside else block')
finally:
    print('Inside finally block')
