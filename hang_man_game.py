import random

word_list = [
    "apple", "river", "mountain", "cloud", "forest", "silver", "energy", "future",
    "ocean", "vision", "planet", "bridge", "shadow", "storm", "dream", "galaxy",
    "flame", "signal", "thunder", "whisper", "breeze", "memory", "harmony",
    "crystal", "echo", "gravity", "journey", "moment", "sunrise", "sunset",
    "motion", "spark", "adventure", "light", "magic", "wonder", "circuit",
    "binary", "vector", "python", "engine", "mirror", "paper", "signal",
    "canvas", "engineer", "random", "silent", "rapid", "gentle", "brave",
    "quantum", "digital", "matrix", "cycle", "orbit", "fusion", "charge",
    "global", "micro", "nano", "wave", "pulse", "glow", "flare", "storm",
    "thread", "system", "module", "device", "future", "nova", "cosmic",
    "ripple", "cluster", "frame", "switch", "pixel", "logic", "signal",
    "phase", "drive", "level", "point", "scale", "core", "node", "field",
    "range", "scope", "shift", "focus", "prime", "trace", "layer", "cycle",
    "unit", "block", "map", "flow"
]

lives = 6

print("Welcome to Hangman!")
print()

stages = [
    r'''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
''',
    r'''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
''',
    r'''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
''',
    r'''
   +---+
   |   |
   O   |
  /|   |
       |
       |
''',
    r'''
   +---+
   |   |
   O   |
  |    |
       |
       |
''',
    r'''
   +---+
   |   |
   O   |
       |
       |
       |
''',
    r'''
   +---+
   |   |
       |
       |
       |
       |
'''
]

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print("Word to guess: " + placeholder)
print()

game_over = False
correct_letters = []

while not game_over:
    print(f"******* Lives: {lives}/6 *******")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed the letter {guess}. Try another letter.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    print()

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print()

        if lives == 0:
            game_over = True
            print("**** YOU LOSE ****")

    if "_" not in display:
        game_over = True
        print("**** YOU WIN ****")

    print(stages[lives])
    print()