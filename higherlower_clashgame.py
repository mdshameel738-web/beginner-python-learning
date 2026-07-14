import random

celebrities = {
    "Elon Musk": 363000000000,
    "Mark Zuckerberg": 260000000000,
    "Jeff Bezos": 240000000000,
    "Bill Gates": 179000000000,
    "Larry Page": 160000000000,
    "Warren Buffett": 152000000000,
    "Bernard Arnault": 149000000000,
    "Jensen Huang": 138000000000,
    "Mukesh Ambani": 109000000000,
    "Cristiano Ronaldo": 669000000,
    "Lionel Messi": 511000000,
    "Selena Gomez": 416000000,
    "Dwayne Johnson": 391000000,
    "Kylie Jenner": 391000000,
    "Ariana Grande": 372000000,
}

print("Welcome to the Higher or Lower Game!")
print()

score = 0
game_over = False

while not game_over:
    # Pick two random celebrities
    celebrity_a = random.choice(list(celebrities.keys()))
    celebrity_b = random.choice(list(celebrities.keys()))
    
    # Make sure they are different
    while celebrity_a == celebrity_b:
        celebrity_b = random.choice(list(celebrities.keys()))
    
    # Get their values
    value_a = celebrities[celebrity_a]
    value_b = celebrities[celebrity_b]
    
    # Display the choices
    print(f"Choice A: {celebrity_a}")
    print(f"Choice B: {celebrity_b}")
    print()
    
    # Determine the winner
    if value_a > value_b:
        correct_answer = "A"
    else:
        correct_answer = "B"
    
    # Ask the user
    guess = input("Who has more wealth? Type A or B: ").upper()
    print()
    
    # Check if correct
    if guess == correct_answer:
        score += 1
        print(f"Correct! Your score is {score}")
        print()
    else:
        game_over = True
        print("Wrong! Game Over!")
        print(f"Your final score: {score}")
        print(f"{celebrity_a}: ${value_a:,}")
        print(f"{celebrity_b}: ${value_b:,}")
