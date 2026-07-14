import random

print("Welcome to Blackjack!")
print()

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Deal cards to player
player_card1 = random.choice(cards)
player_card2 = random.choice(cards)
player_score = player_card1 + player_card2

# Deal cards to computer
computer_card1 = random.choice(cards)
computer_card2 = random.choice(cards)
computer_score = computer_card1 + computer_card2

# Show player's cards
print(f"Your cards: {player_card1}, {player_card2}")
print(f"Your score: {player_score}")
print()

# Show computer's first card
print(f"Computer first card: {computer_card1}")
print()

# Ask player if they want another card
another_card = input("Do you want another card? (yes/no): ").lower()

if another_card == "yes" or another_card == "y":
    player_card3 = random.choice(cards)
    player_score = player_score + player_card3
    print(f"Your new card: {player_card3}")
    print(f"Your new score: {player_score}")
    print()

# Show final results
print("Final Results:")
print(f"Your cards: {player_card1}, {player_card2}, Score: {player_score}")
print(f"Computer cards: {computer_card1}, {computer_card2}, Score: {computer_score}")
print()

# Determine winner
if player_score > 21:
    print("You lost! You went over 21.")
elif computer_score > 21:
    print("You won! Computer went over 21.")
elif player_score > computer_score:
    print("You won!")
elif player_score == computer_score:
    print("It is a draw!")
else:
    print("You lost!")