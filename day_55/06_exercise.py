inputs = [1, 2, 3]  # eval(input())


def logging_decorator(func):
    def wrapper(*args):
        print(f'You called: {func.__name__}{args}')
        print(f'It returned: {func(args[0], args[1], args[2])}')

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
