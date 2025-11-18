import random
import rock_paper_scissors


choice = int(input("What do you choose? Type 0 for Rock,"
                   " 1 for Paper or 2 for Scissors: "))

print(rock_paper_scissors.options[choice])

computer_play = random.randint(0, 2)

print(f"Computer choose: \n{rock_paper_scissors.options[computer_play]}")

if computer_play == choice:
  print("Its a Tie!")
elif computer_play != choice:
  if ((computer_play == 0 and choice == 2)
      or (computer_play == 1 and choice == 0)
      or (computer_play == 2 and choice == 1)):
    print("You Lose!")
  else:
    print("You Win!")
