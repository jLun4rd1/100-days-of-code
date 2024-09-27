from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

more_coffee = 'y'

while more_coffee == 'y':
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'report':
        print(coffee_machine.report())
        print(money_machine.report())
    elif user_choice == 'off':
        more_coffee = 'n'
    elif user_choice in ['espresso','latte','cappuccino']:
        drink = menu.find_drink(user_choice)
        cost = drink.cost
        
        enough = coffee_machine.is_resource_sufficient(drink)
        
        if enough == True:
            payment = False
            while payment == False:
                payment = money_machine.make_payment(cost)
                
            coffee_machine.make_coffee(drink)
                
        more_coffee = input("Do you want to make another order? Type 'y' or 'n': ")
    else:
        (f"Sorry, didn't understand what you meant by '{user_choice}'")

