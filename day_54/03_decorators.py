def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def common(calc_fun, n1, n2):
    return calc_fun(n1, n2)


x = common(add, 1, 2)
print(x)


def outer_func():
    print('I\'m outer')

    def inner_func():
        print('I\'m inner')

    inner_func()


outer_func()


def outer_func_2():
    print('I\'m outer')

    def inner_func():
        print('I\'m inner')

    return inner_func


inner = outer_func_2()
inner()
