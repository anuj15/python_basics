fib = []
a = 1
b = 1
fib.append(a)
fib.append(b)
for i in range(8):
    c = a + b
    a = b
    b = c
    fib.append(c)
new_list = [x ** 2 for x in fib]
print(new_list)

string_list = ['1', '2', '3', '4', '5']
new_list = [int(x) for x in string_list]
print(new_list)

new_list = [x for x in new_list if x % 2 == 0]
print(new_list)
