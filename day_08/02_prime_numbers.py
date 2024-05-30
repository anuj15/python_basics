def is_prime(num):
    factors = 0
    if num in [0, 1]:
        print(f'{num} is Not Prime')
    else:
        for n in range(1, num + 1):
            if num % n == 0:
                factors += 1
        if factors > 2:
            print(f'{num} is Not Prime')
        else:
            print(f'{num} is Prime')


for i in range(100):
    is_prime(i)
