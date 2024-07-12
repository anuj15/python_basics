import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(func):
    def wrapped_func():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)

    return wrapped_func


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        x = i ** 2


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        x = i ** 2


fast_function()
slow_function()
