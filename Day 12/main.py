# Number Guessing Game!
import random
import art

print(art.logo)

numbers_list = []

for number in range(1, 101):
    numbers_list.append(number)

print("I'm thinking of a number between 1 and 100...")
target_number = random.choice(numbers_list)
guess = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    tries = 10
elif difficulty == 'hard':
    tries = 5
else:
    print(f"No such option as {difficulty}. Defaulting to hard")

while guess != target_number and tries > 0:
    print(f'You have {tries} attempts remaining to guess the number.')
    guess = int(input("Make a guess: "))
    
    if guess < target_number:
        print("Too low.")
        print("Guess again")
        tries -= 1
    elif guess > target_number:
        print("Too high.")
        print("Guess again")
        tries -= 1
    else:
        print(f"Congratulations! You guessed the number {target_number}")