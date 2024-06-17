def add(*args):
    sum_all = 0
    for i in args:
        sum_all += i
    print(sum_all)


add(1, 2)


def calc(n, **kwargs):
    n += kwargs.get('add')
    n *= kwargs.get('multiply')
    return n


result = calc(2, add=3, multiply=5)
print(result)
