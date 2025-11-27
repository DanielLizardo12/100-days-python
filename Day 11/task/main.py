from art import logo
import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def add_card_to_hand(current_hand):
    random_card = random.choice(cards)

    if random_card + sum(current_hand) > 21 and 11 in current_hand:
        current_hand[current_hand.index(11)] = 1

    if random_card == 11:
        if sum(current_hand) + 11 > 21:
            return 1

    return random_card

def print_user_cards_and_score(hand, hand_sum):
    print(f"Your cards: {hand}, current score: {hand_sum}")

def print_computer_first_card(card):
    print(f"Computer's fist card: {card}")

def print_final_score(hand, hand_sum):
    return f"final hand: {hand}, final score: {hand_sum}"

def print_user_cards_and_computer_first_card(hand, hand_sum, card):
    print_user_cards_and_score(hand, hand_sum)
    print_computer_first_card(card)

def final_scores(user_hand, user_hand_sum, computer_hand, computer_hand_sum):
    print(f"Your {print_final_score(user_hand, user_hand_sum)}")
    print(f"Computer's {print_final_score(computer_hand, computer_hand_sum)}")

def add_all_cards_for_computer(hand):
    while sum(hand) < 17:
        hand.append(add_card_to_hand(hand))
    return hand

while True:

    if input("Do you wanna play a game of Blackjack? (y/n): ").lower() == "n":
        break

    print("\n" * 20)
    print(logo)
    user_hand = []
    computer_hand = []

    for _ in range(2):
        user_hand.append(add_card_to_hand(user_hand))
        computer_hand.append(add_card_to_hand(computer_hand))

    user_hand_sum = sum(user_hand)
    computer_hand_sum = sum(computer_hand)
    print_user_cards_and_computer_first_card(user_hand,
                                             user_hand_sum, computer_hand[0])

    game_over = False
    while True:
        if input("Get another card? (y/n): ").lower() == "n":
            break
        user_hand.append(add_card_to_hand(user_hand))
        user_hand_sum = sum(user_hand)
        if user_hand_sum > 21:
            computer_hand = add_all_cards_for_computer(computer_hand)
            computer_hand_sum = sum(computer_hand)
            final_scores(user_hand, user_hand_sum,
                         computer_hand,computer_hand_sum)
            print("You went over. You lose 😭")
            game_over = True
            break
        else:
            print_user_cards_and_computer_first_card(
                user_hand, user_hand_sum, computer_hand[0])

    while not game_over:
        computer_hand = add_all_cards_for_computer(computer_hand)
        computer_hand_sum = sum(computer_hand)
        final_scores(user_hand, user_hand_sum,
                     computer_hand, computer_hand_sum)

        if computer_hand_sum > 21:
            print("Opponent went over. You win 😁")
        elif user_hand_sum > computer_hand_sum:
            print("You win 😁")
        elif user_hand_sum < computer_hand_sum:
            print("You lose 😤")
        elif user_hand_sum == computer_hand_sum:
            print("Is a TIE")
        game_over = True