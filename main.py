import random
import os
from art import draw_blackjack_logo

def clear():
    os.system('cls')  # for Windows

user_hand = []
computer_hand = []

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(cards):
    user_hand.extend(random.sample(cards, 2))
    computer_hand.extend(random.sample(cards, 2))


def score_calculator(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_hand, computer_hand):
    if score_calculator(user_hand) == score_calculator(computer_hand):
        return "DRAW"
    elif score_calculator(computer_hand) == 0:
        return "YOU LOSE COMPUTER HAS A BLACK JACK "
    elif score_calculator(user_hand) == 0:
        return " YOU WIN WITH A BLACKJACK"
    elif score_calculator(computer_hand) > 21:
        return "OPPONENT WENT OVER OVER . YOU WIN"
    elif score_calculator(user_hand) > 21:
        return "YOU WENT OVER , YOU LOSE"
    elif score_calculator(user_hand) > score_calculator(computer_hand):
        return "YOU WIN"
    else:
        return "YOU LOSE"


def play_game() :
    draw_blackjack_logo()
    is_game_over = False

    deal_cards(cards)

    while not is_game_over :
        user_score = score_calculator(user_hand)
        computer_score = score_calculator(computer_hand)

        print(f"Your cards :{user_hand} current score is {user_score} :")
        print(f"Opponent first card is : {computer_hand[0]}")

        if user_score == 0 or computer_score== 0 or user_score > 21 :
            is_game_over = True
        else :
            user_should_deal=input("type y : to get another card , type n : to pass : ")
            if user_should_deal == "y" :
                user_hand.append(random.choice(cards))
            else :
                is_game_over= True
    while computer_score != 0 and computer_score <17 :
        computer_hand.append(random.choice(cards))
        computer_score=score_calculator(computer_hand)

    print(f"Your final hand : {user_hand} , and your final score is : {user_score} ")
    print(f"Computer final hand is : {computer_hand} with the final score of : {computer_score}")
    print(compare(user_hand , computer_hand))


while input("Do you want to play a game of BlackJack? Type 'y' to play and 'n' to quite : ") == "y" :
    clear()
    play_game()


