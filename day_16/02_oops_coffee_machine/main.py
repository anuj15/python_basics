from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
stop_machine = False

while not stop_machine:
    items = menu.get_items()
    get_order = input(f'What would you like? ({items}): ').lower()
    if get_order == 'off':
        stop_machine = True
    elif get_order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif get_order in items:
        drink = menu.find_drink(get_order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print('Invalid Input.')
        break
