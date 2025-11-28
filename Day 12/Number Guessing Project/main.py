import sys

from art import logo

import random

number = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempts = 5

if difficulty == "easy":
    attempts = 10

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {guess}")
        sys.exit()
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")

    attempts -= 1

    if attempts > 0:
        print("Guess again.")


print("You've run out of guesses, you lose.")

