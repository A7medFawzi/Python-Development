from art import logo
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
print(logo)
print('||| Welcome to Coffee Machine,Choose Your drink 👇🏻 |||')
money = 0
end = False
cost = 0
milk_resource = resources["milk"]
water_resource = resources["water"]
coffee_resource = resources["coffee"]

while not end:
    choose_drink = input(" \n What would you like to drink? (espresso/latte/cappuccino): ").lower()

    if choose_drink == "off":
        print("Thank You for use the coffee machine, GoodBye 👋!")
        end = True
        break
    elif choose_drink == "report":
        print("\nThere is the machine resources:")
        print(f"\nWater:{water_resource}ml\nMilk: {milk_resource}ml\nCoffee: {coffee_resource}g\nMoney: ${money}")
        continue

    water = MENU[choose_drink]["ingredients"]["water"]
    coffee = MENU[choose_drink]["ingredients"]["coffee"]
    cost = MENU[choose_drink]["cost"]

    if water_resource < water:
        print("\nSorry there is not enough water 😓.")
        continue
    else:

        if "milk" in MENU[choose_drink]["ingredients"]:
            milk = MENU[choose_drink]["ingredients"]["milk"]
        else:
            milk = 0

    print("\nPlease insert coins 💰!")

    insert_money1 = int(input("how many quarters?: ")) * 0.25
    insert_money2 = int(input("how many dimes?: ")) * 0.10
    insert_money3 = int(input("how many nickles?: ")) * 0.05
    insert_money4 = int(input("how many pennies?: ")) * 0.01

    all_coin = insert_money1 + insert_money2 + insert_money3 + insert_money4

    if all_coin < cost:
        print("\nSorry that's not enough money. Money refunded 💵.")
        continue
    else:
        money += cost
        milk_resource -= milk
        water_resource -= water
        coffee_resource -= coffee

    change = all_coin - cost
    print(f"\nHere is ${round(change, 2)} in change 💳.")
    print(f"Here is your {choose_drink} ☕️. Enjoy!")
