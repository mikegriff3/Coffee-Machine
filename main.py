import sys

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
}


def prompt():
    return input("What would you like? Espresso, Latte, or Cappuccino: ")


def turn_off():
    sys.exit()


def check_resources(ingredients, current_resources, item):
    if item != "espresso":
        if current_resources['milk'] < ingredients['milk']:
            print("Sorry there is not enough milk.")
            run()

    if current_resources['water'] < ingredients['water']:
        print("Sorry there is not enough water.")
        run()
    elif current_resources['coffee'] < ingredients['coffee']:
        print("Sorry there is not enough coffee.")
        run()
    else:
        return


def get_payment(item, order):
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total_payment = quarters + dimes + nickels + pennies
    if total_payment < item["cost"]:
        print("Sorry that is not enough money. Money refunded.")
        run()
    elif total_payment > item["cost"]:
        change = round(total_payment - item["cost"], 2)
        print(f"Here is ${change} in change.")
        return
    else:
        return


def deduct_resources(item, order):
    resources["water"] -= item["water"]
    resources["coffee"] -= item["coffee"]
    if order != "espresso":
        resources["milk"] -= item["milk"]


def run():
    selection = prompt().lower()
    if selection == "off":
        turn_off()
    elif selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    elif selection == "espresso":
        check_resources(MENU['espresso']['ingredients'], resources, "espresso")
        print("The price of this item is $1.50. Please insert coins now.")
        get_payment(MENU['espresso'], "espresso")
        deduct_resources(MENU['espresso']['ingredients'], "espresso")
        print(f"Here is your espresso. Enjoy!")
    elif selection == "latte":
        check_resources(MENU['latte']['ingredients'], resources, "latte")
        print("The price of this item is $2.50. Please insert coins now.")
        get_payment(MENU['latte'], "latte")
        deduct_resources(MENU['latte']['ingredients'], "latte")
        print(f"Here is your latte. Enjoy!")
    elif selection == "cappuccino":
        check_resources(MENU['cappuccino']['ingredients'], resources, "cappuccino")
        print("The price of this item is $3.00. Please insert coins now.")
        get_payment(MENU['cappuccino'], "cappuccino")
        deduct_resources(MENU['cappuccino']['ingredients'], "cappuccino")
        print(f"Here is your cappuccino. Enjoy!")
    else:
        print("Invalid selection. Please choose again.")
        run()

    run()


run()
