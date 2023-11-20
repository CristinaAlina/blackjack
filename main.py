############### Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
from replit import clear


def calculate_score(desk_player):
    """Take a list of cards and returns the score calculated from the cards"""
    if sum(desk_player) > 21 and 11 in desk_player:
        desk_player.remove(11)
        desk_player.append(1)
    return sum(desk_player)


def calc_final_score_computer(desk_computer):
    """Take the computer's list of cards and returns the score calculated from the cards"""
    score_computer = calculate_score(desk_computer)
    while score_computer < 17:
        draw_one_card(desk_computer)
        score_computer = calculate_score(desk_computer)
    return score_computer


def draw_one_card(desk_player):
    """Add a new random card to the desk"""
    desk_player.append(random.choice(cards))
    return desk_player


def blackjack_final_statement(score_user, score_computer):
    """Compare the scores and print the conclusion"""
    if score_user > 21 and score_computer > 21:
        # If you and the computer are both over, you lose
        print("You went over. You lose 😤")
    elif score_user == score_computer:
        print("Draw 🙃")
    elif score_user == 21:
        print("Win with a Blackjack 😎")
    elif score_user > 21:
        print("You went over. You lose 😭")
    elif score_computer > 21:
        print("Opponent went over. You win 😁")
    elif score_computer > score_user:
        print("You lose 😤")
    else:
        print("You win 😃")


def print_current_desks(score_user, desk_user, card_computer):
    """Print the current status of cards for each player"""
    print(f"Your cards: {desk_user}, current score: {score_user}")
    print(f"Computer's first card: {card_computer}")


def print_final_desks(score_user, score_computer, desk_user, desk_computer):
    """Print the final status of cards for each player"""
    print(f"  Your final hand: {desk_user}, final score: {score_user}")
    print(
        f"  Computer's final hand: {desk_computer}, final score: {score_computer}"
    )


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    """Play the game"""
    desk_user = []
    desk_computer = []
    game_over = False
  
    print(logo)
    # draw two cards at the beginning of the game
    for _ in range(2):
        draw_one_card(desk_user)
        draw_one_card(desk_computer)

    score_user = calculate_score(desk_user)

    print_current_desks(score_user, desk_user, desk_computer[0])

    if score_user == 21:
        game_over = True
    else:
        draw_again = True
        while draw_again:
            draw = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            while not draw in ['y', 'n']:
                draw = input(
                    "Invalid input. Type 'y' to get another card, type 'n' to pass: "
                )

            if draw == 'n':
                game_over = True
                draw_again = False
            else:
                draw_one_card(desk_user)
                score_user = calculate_score(desk_user)
                print_current_desks(score_user, desk_user,
                                    desk_computer[0])
                if score_user >= 21:
                    game_over = True
                    draw_again = False

    if game_over == True:
        score_computer = calc_final_score_computer(desk_computer)
        print_final_desks(score_user, score_computer, desk_user,
                          desk_computer)
        blackjack_final_statement(score_user, score_computer)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    blackjack()
  