MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

profit = 0
resources  = {
        "water":300,
        "milk":200,
        "coffee":100,
        
}

def is_resources_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item,0):
            print(f"Sorry there is not enough {item},")
            return False
    return True

def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?."))*0.25
    total += int(input("How many dimes?."))*0.1
    total += int(input("How many nickles?."))*0.05
    total += int(input("How many pennies?."))*0.01
    return total

def is_transactions_successful(money_received, drink_cost):
    """Return True if payment is accepted or False if insufficient."""
    if money_received >=drink_cost:
        global profit
        change = round(money_received - drink_cost,2)
        profit += drink_cost
        if change >= 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")



#TODO: 1. Print report of all coffee machine resources.
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in  MENU:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transactions_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
    else:
        print("Invalid input. Please choose espresso, latte, or cappuccino.")


            

