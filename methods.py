import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with Blackjack 😎"
    elif user_score > 21:
        return "You went over. You Lose 😭"
    elif computer_score > 21:
        return "Opponent went over.You win 😁"
    elif user_score > computer_score:
        return "You Win 😃"
    return "You Lose 😤"


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
