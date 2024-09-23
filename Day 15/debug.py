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

# def get_drink_data(beverage):
#     beverage = MENU[beverage]
    
#     ingredients = beverage['ingredients']
#     water = ingredients['water']
#     coffee = ingredients['coffee']
#     if beverage == 'latte' or beverage == 'cappuccino':
#         milk = ingredients['milk']
#     else:
#         milk = 0
    
#     cost = beverage['cost']
    
#     return water, coffee, milk, cost

# TODO 1.2 Check sufficient resources
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
            coin_value = coins[coin]
            valid = False
            while valid == False:
                try:
                    amount = int(input(f'How many {coin} (${coin_value})?')) * coin_value
                    total_inserted += amount
                    print(f'Inserted total of ${amount} in {coin}')
                    valid = True
                except ValueError:
                    print(f"It seems like you didn't insert a numerical value by typing {amount}. Try typing a digit, like '2' or '3'")
        # try:
        #     dimes = int(input('How many dimes ($0.10)?')) * 0.10
        #     total_inserted += dimes
        #     print(f'Inserted total of ${dimes} in dimes')
        # except ValueError:
        #     print(f"It seems like you didn't insert a numerical value by typing {dimes}. Try typing a digit, like '2' or '3'")
        
        # try:
        #     nickels = int(input('How many nickels ($0.05)?')) * 0.05
        #     total_inserted += nickels
        #     print(f'Inserted total of ${nickels} in nickels')
        # except ValueError:
        #     print(f"It seems like you didn't insert a numerical value by typing {nickels}. Try typing a digit, like '2' or '3'")
        
        # try:
        #     pennies = int(input('How many pennies ($0.01)?')) * 0.01
        #     total_inserted += pennies
        #     print(f'Inserted total of ${pennies} in pennies')
        # except ValueError:
        #     print(f"It seems like you didn't insert a numerical value by typing {pennies}. Try typing a digit, like '2' or '3'")
        
        if total_inserted >= beverage_cost:
            change = round(total_inserted - beverage_cost, 2)
            print(f"The beverage cost was ${beverage_cost}. You inserted a total of ${total_inserted}.")
            if change != 0:
                print(f"Here's your change of ${change}")
            successful_transaction = True
        else:
            required_amount = round(beverage_cost - total_inserted, 2)
            print(f"You inserted a total of ${total_inserted}, but you still need to insert ${required_amount}")

    
                

report = get_machine_info()

# TODO 1. Print Report to know about resources
# TODO 1.1 Ask what the customer wants
user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
if user_choice == 'report':
    print(report)
elif user_choice in ['espresso','latte','cappuccino']:
    drink = user_choice
    # drink_water, drink_coffee, drink_milk, drink_cost = get_drink_data(drink)
    enough, drink_cost = check_for_resources_and_price(beverage=drink)
    if enough == True:
        insert_coins(beverage_cost=drink_cost, coins=coins)


        

# TODO 2. Process Coins
# TODO 2.1 As soon as the user selects a drink, print the price
# TODO 2.2 Check successful transaction

# TODO 3. Make the coffee
# TODO 3.1 Deduct the resources: