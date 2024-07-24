import main


while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while play != "y" and play != "n":
        play = input("Please type 'y' or 'n': ")
    if play == "y":
        main.play_game()
    else:
        break
