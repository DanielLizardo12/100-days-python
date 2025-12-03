import random
import art
from game_data import data

current_winner = random.choice(data)

def print_pick_desc(pick):
    return f"{pick["name"]} a {pick["description"]}, from {pick["country"]}"

score = 0
while True:
    print(art.logo)
    second_runner = random.choice(data)

    while second_runner == current_winner:
        second_runner = random.choice(data)

    current_winner["choice"] = "a"
    second_runner["choice"] = "b"
    runners = [current_winner, second_runner]

    print(f"Compare A: {print_pick_desc(current_winner)}")
    print(art.vs)
    print(f"Compare B: {print_pick_desc(second_runner)}")

    winner = max(runners, key=lambda x: x["follower_count"])

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice == winner["choice"]:
        score += 1
        current_winner = winner
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        break