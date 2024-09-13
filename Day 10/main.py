# Calculator Project
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dictionary_of_operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

keep_going = True
more_operations = 'n'

while keep_going == True:
    print(25 * '\n')
    print(art.logo)
    
    if more_operations == 'n':
        first_number = int(input("What's the first number?: "))
    
    for symbol in dictionary_of_operations:
        print(symbol)
        
    operation_input = input("Pick an operation: ")
    operation = dictionary_of_operations[operation_input]
    
    second_number = int(input("What's the second number?: "))

    result = operation(first_number, second_number)
    print(f'{first_number} {operation_input} {second_number} = {result}')
        
    more_operations = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation. You can also type 'e' to exit.\n")
    
    if more_operations == 'y':
        first_number = result
    elif more_operations == 'e':
        keep_going = False