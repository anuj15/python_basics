num = [1, 2, 3]
new_list = [x + 1 for x in num]
print(new_list)

name = 'Anuj'
new_list = [x for x in name]
print(new_list)

new_list = [x * 2 for x in range(1, 5)]
print(new_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
new_list = [x for x in names if len(x) < 5]
print(new_list)

new_list = [x.upper() for x in names if len(x) > 5]
print(new_list)
