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

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01   
}

def get_machine_info():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    try:
        money = resources['money']
    except:
        resources['money'] = 0.0
        money = resources['money']
        
    report = f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"

    return report

def check_for_resources_and_price(beverage):
    enough = True 
    for ingredient in MENU[beverage]['ingredients']:
        if enough == True:
            bevarage_value = MENU[beverage]['ingredients'][f'{ingredient}']
            machine_value = resources[ingredient]
            if bevarage_value > machine_value:
                print(f'Sorry, there is not enough {ingredient}')
                enough = False  
        
    if enough:
        beverage_cost = MENU[beverage]['cost']
        print(f'Ready to make some {beverage}! It will cost ${beverage_cost}\n')
    else:
        beverage_cost = 0    
               
    return enough, beverage_cost

def insert_coins(beverage_cost, coins):
    successful_transaction = False
     
    total_inserted = 0
    
    while successful_transaction == False:
        print("Please, insert coins.")
        
        for coin in coins:
            valid = False
            coin_value = coins[coin]
            
            while valid == False:
                try:
                    amount = int(input(f'How many {coin} (${coin_value})?')) * coin_value
                    total_inserted += amount
                    print(f'Inserted total of ${amount} in {coin}')
                    valid = True
                except ValueError:
                    print(f"It seems like you didn't insert a numerical value by typing {amount}. Try typing a digit, like '2' or '3'")
        
        if total_inserted >= beverage_cost:
            change = round(total_inserted - beverage_cost, 2)
            print(f"The beverage cost was ${beverage_cost}. You inserted a total of ${total_inserted}.")
            if change != 0:
                print(f"Here's your change of ${change}")
            successful_transaction = True
        else:
            required_amount = round(beverage_cost - total_inserted, 2)
            print(f"You inserted a total of ${total_inserted}, but you still need to insert ${required_amount}")

def make_and_deliver_coffee(beverage, beverage_cost, resources):
    for ingredient in MENU[beverage]['ingredients']:
        resources[ingredient] -= MENU[beverage]['ingredients'][ingredient]
    
    try:
        resources['money'] += beverage_cost
    except:
        resources['money'] = beverage_cost
    print(f"Here's your {beverage}. Enjoy!")
    return resources

def main():
    more_coffee = 'y'
    user_choice = ''

    while more_coffee == 'y' and user_choice != 'off':
        report = get_machine_info()

        user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if user_choice == 'report':
            print(report)
        elif user_choice ==  'off':
            print(f'Turning machine off...')
        elif user_choice in ['espresso','latte','cappuccino']:
            drink = user_choice
            enough, drink_cost = check_for_resources_and_price(beverage=drink)
            if enough == True:
                insert_coins(beverage_cost=drink_cost, coins=coins)
                resources = make_and_deliver_coffee(beverage=drink, beverage_cost=drink_cost, resources=resources)
            more_coffee = input("Do you want to make another order? Type 'y' or 'n'")
        else:
            print(f"Sorry, didn't understand what you meant by '{user_choice}'")

main()