from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

machine = CoffeeMaker()
money_in = MoneyMachine()
menu = Menu()

while machine_on:
    selection = input(f"What would you like? ({menu.get_items()}): ")

    if selection == "espresso" or selection == "latte" or selection == "cappuccino":
        my_coffee = menu.find_drink(selection)
        if machine.is_resource_sufficient(my_coffee):
            if money_in.make_payment(my_coffee.cost):
                machine.make_coffee(my_coffee)
    elif selection == "report":
        machine.report()
        money_in.report()
    elif selection == "off":
        machine_on = False
    else:
        print("Wrong selection")
