import assets
import random

list = [assets.rock, assets.paper, assets.scissors]
index_list = [0, 1, 2]

player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\nR: '))

random_option = random.choice(index_list)

computer = random.choice(index_list)
computer_choice = list[computer]

if int(player) in index_list:
    print(player)
    player_choice = list[player]
    print(player_choice)
else:
    print('Remember to type a valid number! This time around I chose this for you:')
    player = random_option

    player_choice = list[player]    
    print(player_choice)
    
print('Computer chose:')
print(computer_choice)

## More logical way
if player == 2 and computer == 0:
    print('You lose!')
elif player == 0 and computer == 2:
    print('You win!')
elif player > computer:
    print('You win!')
elif computer > player:
    print('You lose!')
elif player == computer:
    print('It\'s a draw!')

## More descriptive way
# if player_choice == assets.rock and computer_choice == assets.paper:
#     print('You lose!')
# elif player_choice == assets.rock and computer_choice == assets.scissors:
#     print('You win!')
# elif player_choice == assets.paper and computer_choice == assets.scissors:
#     print('You lose!')
# elif player_choice == assets.paper and computer_choice == assets.rock:
#     print('You win!')
# elif player_choice == assets.scissors and computer_choice == assets.rock:
#     print('You lose!')
# elif player_choice == assets.scissors and computer_choice == assets.paper:
#     print('You win!')
# else:
#     print('It\'s a draw!')
