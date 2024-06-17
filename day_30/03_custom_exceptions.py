# try:
#     print('Inside try block')
#     1 + 'test'
# except TypeError as e:
#     print('Inside except block')
# else:
#     print('Inside else block')
# finally:
#     print('Inside finally block')
#     raise KeyError('This is a self generated error')

height = float(input('Enter height in meters: '))
if height > 3:
    raise ValueError('Human height cannot be greater than 3 meters.')
weight = float(input('Enter weight in kilograms: '))
bmi = weight // height ** 2
print(bmi)
