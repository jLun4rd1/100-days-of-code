import art
import game_data
import random
import os

def get_indexes(idxA, idxB, first_choice=False):
    while idxA == idxB:
        if first_choice == True:
            idxA = random.randint(1, (length - 1))
        idxB = random.randint(1, (length - 1))
    
    return idxA, idxB

def get_data(idx):
    name = data[idx]['name']
    follower_count = data[idx]['follower_count']
    description = data[idx]['description']
    country = data[idx]['country']
    compare = f'{name}, a {description}, from {country}'
    
    return follower_count, compare

# def get_B_data(idxB): << Unnecessarily repeating, since the only thing we need is the index
#     nameB = data[idxB]['name']
#     follower_countB = data[idxB]['follower_count']
#     descriptionB = data[idxB]['description']
#     countryB = data[idxB]['country']
#     compareB = f'Against B: {nameB}, a {descriptionB}, from {countryB}'
    
#     return follower_countB, compareB

def compare_A_and_B(flwr_cnt_A, flwr_cnt_B, statement_A, statement_B, score):
    print(statement_A)
    print(art.vs)
    print(statement_B)

    adequate_answer = False
    while adequate_answer == False:
        player = input("Who has more followers? Type 'A' or 'B': ").lower()
        if player not in ['a','b']:
            print(f"Sorry, didn't understand what you meant by '{player}'. Let's try again!")
        else:
            adequate_answer = True
            
    if player == 'a' and flwr_cnt_A > flwr_cnt_B:
        got_it_right = True
        score += 1
    elif player == 'a' and flwr_cnt_A < flwr_cnt_B:
        got_it_right = False
        score = score
    elif player == 'b' and flwr_cnt_B > flwr_cnt_A:
        got_it_right = True
        score += 1
    else:
        got_it_right = False
        score = score
    
    return score, got_it_right

def play_a_round(idxA, idxB, score, frst_choice):
    idxA, idxB = get_indexes(indexA, indexB, frst_choice)

    follower_countA, compareA = get_data(idxA)
    compareA = 'Compare A: ' + compareA

    follower_countB, compareB = get_data(idxB)
    compareB = 'Against B: ' + compareB
                
    score, result = compare_A_and_B(follower_countA, follower_countB, compareA, compareB, score)
    
    return score, result, idxA, idxB

data = game_data.data
length = len(data)

score = 0

indexA = 0
indexB = 0

result = True

first_choice = True

while result == True:
    print(art.logo)
    
    if first_choice == False:
        print(f"You've got it! Current Score: {score}")
    
    score, result, indexA, indexB = play_a_round(indexA, indexB, score, first_choice)
    
    indexA = indexB
    
    first_choice = False
    
    os.system('cls')

print(art.logo)
print(f"Sorry, that's wrong! Final score: {score}")