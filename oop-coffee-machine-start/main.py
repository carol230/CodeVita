from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

machineWorking = True

while machineWorking:
    options = menu.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino/):")
    if choice == 'off':
        machineWorking = False
    elif choice == "report":
        coffeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
             coffeMaker.make_coffee(drink)


