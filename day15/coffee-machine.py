def on():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.00
    }

    def show_resos():
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {resources['money']}")

    def turn_off():
        quit()

    # check if the machine has enough of each resource to make the coffee
    def have_enough_resos(type_of_coffee, resos):
        if resos['water'] < MENU[type_of_coffee]['ingredients']['water']:
            return False
        elif resos['milk'] < MENU[type_of_coffee]['ingredients']['milk']:
            return False
        elif resos['coffee'] < MENU[type_of_coffee]['ingredients']['coffee']:
            return False
        else:
            return True

    def enough_money(coffee_type, money):
        if MENU[coffee_type]['cost'] > money:
            return False
        else:
            return True

    def recalc_reso(resos, coffee_type):
        resos['water'] -= MENU[coffee_type]['ingredients']['water']
        resos['milk'] -= MENU[coffee_type]['ingredients']['milk']
        resos['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
        resos['money'] += MENU[coffee_type]['cost']

    def make_change_give_coffee(money_paid, type_coffee):
        print(f"Your change is {money_paid - MENU[type_coffee]['cost']}")
        print(f"Here is you {selected_coffee} ☕ enjoy!")

    running = False
    while not running:

        selected_coffee = input("What kind of coffee do you want? espresso, latte, or cappuccino")
        if selected_coffee == 'off':
            turn_off()
        elif selected_coffee == 'report':
            show_resos()
        elif selected_coffee == 'latte' or selected_coffee == 'espresso' or selected_coffee == 'cappuccino':

            quarters = float(input("How many quarters?")) * .25
            dimes = float(input("How many dimes?")) * .10
            nickels = float(input("How many nickels?")) * .05
            pennys = float(input("How many pennies?")) * .01
            total_money = round(quarters + dimes + nickels + pennys, 3)
            if have_enough_resos(selected_coffee, resources) is False:
                print("Sorry not enough resources to fulfill your order. Money refunded")
            elif enough_money(selected_coffee, total_money) is False:
                print("Sorry not enough Money to pay for your order. Money refunded")
            else:
                recalc_reso(resources, selected_coffee)
                make_change_give_coffee(total_money, selected_coffee)


on()
