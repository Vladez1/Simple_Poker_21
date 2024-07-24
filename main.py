import methods
import art


def play_game():
    methods.clear()
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(methods.deal_card())
        computer_cards.append(methods.deal_card())
    while not is_game_over:
        user_score = methods.calculate_score(user_cards)
        computer_score = methods.calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(methods.deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(methods.deal_card())
        computer_score = methods.calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(methods.compare(user_score, computer_score))
