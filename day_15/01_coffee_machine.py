from data import MENU, resources

money = 0


def print_report():
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")


def enough_resources(drink):
    if MENU[drink]['ingredients']['water'] > resources['water']:
        print('Sorry, there is not enough water.')
        return False
    elif MENU[drink]['ingredients']['coffee'] > resources['coffee']:
        print('Sorry, there is not enough coffee.')
        return False
    elif drink != 'espresso' and MENU[drink]['ingredients']['milk'] > resources['milk']:
        print('Sorry, there is not enough milk.')
        return False
    else:
        return True


def update_resources(drink):
    global money
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    if drink != 'espresso':
        resources['milk'] = MENU[drink]['ingredients']['milk']
    money += MENU[drink]['cost']


def process_coins(drink):
    print('Pleas insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    money_entered = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    money_needed = MENU[drink]['cost']
    if money_entered < money_needed:
        print('Sorry, that\'s not enough money. Money refunded.')
        return False
    elif money_entered > money_needed:
        change = round(money_entered - money_needed, 2)
        print(f'Here\'s ${change} dollars in change.')
        return True
    else:
        return True


def coffee_machine():
    machine_in_use = True
    while machine_in_use:
        user_input = input('What would you like? (espresso / latte / cappuccino): ').lower()
        if user_input == 'off':
            machine_in_use = False
        elif user_input == 'report':
            print_report()
        elif user_input in ['espresso', 'latte', 'cappuccino']:
            if enough_resources(user_input):
                if process_coins(user_input):
                    update_resources(user_input)
                    print(f'Here is your {user_input} ☕. Enjoy!')
        else:
            print('Invalid input')
            return


coffee_machine()
