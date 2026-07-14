import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """ 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player_choice = int(input("What will you choose? If rock type 1, if paper type 2, if scissors type 3: "))

if player_choice == 1:
    print(rock)
elif player_choice == 2:
    print(paper)
else:
    print(scissors)

game = random.randint(1, 3)
print("Computer choice:")
if game == 1:
    print(rock)
elif game == 2:
    print(paper)
else:
    print(scissors)

if player_choice == game:
    print("It's a draw!")
elif (player_choice == 1 and game == 3) or (player_choice == 2 and game == 1) or (player_choice == 3 and game == 2):
    print("You have won the game!")
else:
    print("You have lost the game!")