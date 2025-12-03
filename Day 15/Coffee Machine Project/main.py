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
    "money": 0.0
}

type_of_change = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "pennie": 0.01,
}

def print_report():
    for item in resources:
        if item == "coffee":
            value_of_item = f"{resources[item]}g"
        elif item == "money":
            value_of_item = f"${resources[item]}"
        else:
            value_of_item = f"{resources[item]}ml"
        print(f"{item.capitalize()}: {value_of_item}")

def coins_to_total():
    total = 0

    print("Please insert coins.")
    for coin in type_of_change:
        total += int(input(f"how many {coin}s?: ")) * type_of_change[coin]

    return round(total, 2)

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    new_resources = resources.copy()

    if choice in MENU:
        sufficient_resources = True
        for ingredient in MENU[choice]["ingredients"]:
            new_resources[ingredient] = (
                new_resources[ingredient]
                - MENU[choice]["ingredients"][ingredient])
            if new_resources[ingredient] < 0:
                print(f"Sorry there is not enough {ingredient}.")
                sufficient_resources = False
                break

        if sufficient_resources:
            choice_cost = MENU[choice]["cost"]
            print(f"the cost of the {choice} is ${choice_cost}")
            user_paid = coins_to_total()

            if user_paid >= choice_cost:
                if user_paid > choice_cost:
                    print(f"Here is ${user_paid - choice_cost} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
                new_resources["money"] = new_resources["money"] + choice_cost
                resources = new_resources
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif choice == "report":
        print_report()

    elif choice == "off":
        sys.exit()

    else:
        print("please select a valid option")