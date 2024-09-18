# LET'S PLAY SOME BLACKJACK, BABY!!
import art
import random
import re
import os

def draw_a_card(suits:list, logo:dict, card_n:dict) -> str:
    suits_choice = random.choice(suits)

    card_number = random.choice(card_n[suits_choice])
    card_n[suits_choice].remove(card_number)

    card_logo = logo[suits_choice]
    card = f"{card_number}" + f"{card_logo}"
    
    return card, card_number, card_n

def player_plays(player_score, player_cards_list, card_n_dict):
    player_card, player_card_n, card_n_dict = draw_a_card(suits=suits_list, logo=logo_dict, card_n=card_n_dict)
    player_cards_list.append(player_card)
    player_score.append(player_card_n)
    
    return player_score, card_n_dict

def computer_plays(computer_score, computer_cards_list, card_n_dict):
    computer_card, computer_card_n, card_n_dict = draw_a_card(suits=suits_list, logo=logo_dict, card_n=card_n_dict)
    computer_cards_list.append(computer_card)
    computer_score.append(computer_card_n)
    
    return computer_score, card_n_dict
    
def print_info(player_cards_list, player_score, computer_cards_list):
    print(f"Your cards: {player_cards_list}, current score: {sum(player_score)}")
    print(f"Computer's first card: {computer_cards_list[0]}")

def print_final_info(player_cards_list, player_score, computer_cards_list, computer_score):
    print(f"Your final hand: {player_cards_list}, final score: {sum(player_score)}")
    print(f"Computer's final hand: {computer_cards_list}, final score: {sum(computer_score)}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    
    suits_list = ['clubs', 'hearts', 'spades', 'diamonds']
    logo_dict = {
        'clubs': '♣', 
        'hearts': '♥',
        'spades': '♠',
        'diamonds': '♦'
        
    }
    card_n_dict = {
        'clubs': [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        'hearts': [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        'spades': [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        'diamonds': [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    }

    print(art.logo)

    win_lose = False

    player_cards_list = []
    player_score = []

    computer_cards_list = []
    computer_score = []

    for index in range(0, 2):
        player_score, card_n_dict = player_plays(player_score, player_cards_list, card_n_dict)
        computer_score, card_n_dict = computer_plays(computer_score, computer_cards_list, card_n_dict)

    if sum(player_score) == 21:
        print_final_info(player_cards_list, player_score, computer_cards_list, computer_score)
        print('You win! ☺')
        win_lose = True
    elif sum(computer_score) == 21:
        print_final_info(player_cards_list, player_score, computer_cards_list, computer_score)
        print('You lose! ☹')
        win_lose = True

    if win_lose == False:
        print_info(player_cards_list, player_score, computer_cards_list)

    keep_going = True

    while keep_going == True and win_lose == False: 
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if another_card == 'y':
            player_score, card_n_dict = player_plays(player_score, player_cards_list, card_n_dict)
            if 11 in player_score and sum(player_score) > 21:
                player_score.remove(11)
                player_score.append(1)
                player_cards_list = [re.sub('^11','1', card) for card in player_cards_list]
                print_info(player_cards_list, player_score, computer_cards_list)
            elif sum(player_score) > 21:
                print_final_info(player_cards_list, player_score, computer_cards_list, computer_score)
                print('You lose! ☹')
                keep_going = False
                win_lose = True
            elif sum(player_score) == 21:
                print_final_info(player_cards_list, player_score, computer_cards_list, computer_score)
                print('You win! ☺')
                keep_going = False
                win_lose = True
            else:
                print_info(player_cards_list, player_score, computer_cards_list)
        elif another_card == 'n':
            keep_going = False

    has_printed = False
        
    if win_lose == False:     
        while sum(computer_score) <= 16:            
            computer_score, card_n_dict = computer_plays(computer_score, computer_cards_list, card_n_dict)
            if 11 in computer_score and sum(computer_score) > 21:
                computer_score.remove(11)
                computer_score.append(1)
                computer_cards_list = [re.sub('^11','1', card) for card in computer_cards_list]
            if sum(computer_score) > 21:
                print_final_info(player_cards_list, player_score, computer_cards_list, computer_score)
                print('You win! ☺')
                win_lose = True
                has_printed = True
            elif sum(computer_score) == 21:
                print_final_info(player_cards_list, player_score, computer_cards_list, computer_score)
                print('You lose! ☹')
                win_lose = True
                has_printed = True
        
        if has_printed == False:
            print_final_info(player_cards_list, player_score, computer_cards_list, computer_score)
            
            if sum(computer_score) > sum(player_score):
                print('You lose! ☹')
            elif sum(player_score) > sum(computer_score):
                print('You win! ☺')
            else:
                print("It's a tie!")