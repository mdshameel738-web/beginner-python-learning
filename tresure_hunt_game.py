
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Which way would you like to turn: left or right? ")
if direction == "left":
    print("You have passed to the next stage.")
else:
    print("Game over! You fell into a trap.")
print("You are at the sea shore at the current time.")
print()
swim = input("Would you like to swim or wait? ")
if swim == "wait":
    print("Wow! You passed another stage!")
else:
    print("Game over! You were eaten by sharks.")
print("A sudden breakdown from the ground - three mysterious doors appear!")
print()
door = input("Which door will you choose: red, yellow, or blue? ")
if door == "yellow":
    print("Bravo! You won the game!")
    print("GAME CLEARED")
elif door == "blue":
    print("Game over! You were eaten by monsters.")
elif door == "red":
    print("Game over! You were burned to death.")
else:
    print("GAME OVER!")