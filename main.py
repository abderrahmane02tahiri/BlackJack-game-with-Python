import random
from art import logo
from typing import List, Any

cards: list[int | Any] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
computer_hand = []


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
