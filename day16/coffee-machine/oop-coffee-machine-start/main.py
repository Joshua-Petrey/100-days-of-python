from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
maker = CoffeeMaker()


running = True
while running:

    options = menu.get_items()
    users_coffee = input(f"What kind of coffee do you want? {options}\n")

    if users_coffee == 'report':
        maker.report()
        money.report()
    elif users_coffee == 'off':
        running = False
    else:
        drink = menu.find_drink(users_coffee)
        if maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                maker.make_coffee(drink)
