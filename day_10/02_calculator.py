from calcualtor_ascii_art import logo


# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiple
def mul(n1, n2):
    return n1 * n2


# Divide
def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return 0


calc_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    print(logo)
    continue_calc = True
    num1 = float(input('What\'s the first number?: '))
    for operator in calc_dict:
        print(operator)
    while continue_calc:
        op = input('Pick an operation: ')
        num2 = float(input('What\'s the next number?: '))
        result = 0
        if op in calc_dict:
            result = calc_dict[op](num1, num2)
        else:
            print(f'{op} is an invalid operator. Exiting.')
        print(f'{num1} {op} {num2} = {result}')
        flag = input(f'Type \'y\' to continue calculating with {result}, or type \'n\' to exit: ')
        if flag == 'y':
            num1 = result
        elif flag == 'n':
            calculator()
        else:
            continue_calc = False


calculator()
