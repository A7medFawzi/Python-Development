from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable
from art import logo

my_table = PrettyTable()

my_table.add_column("Drink",["latte","espresso","cappuccino"])
my_table.add_column("Price",["2.5$","1.5$","3$"])

print("Welcome to Coffee Machine")
print(logo)
print(my_table)
items = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    order = input(f"What would you like? ({items.get_items()}): ").lower()
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        is_on= False
        print("Thank You For Using Coffee Machine ,GoodBye!")
    else:
        drink = items.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else :
            pass
