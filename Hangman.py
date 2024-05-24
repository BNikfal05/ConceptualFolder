'''Welcome to Hangman by the uploader of the document
I have used my knowledge in python to make a basic hangman game for 
fun and store it on github as a test'''

import random as rand

words = ["gallows", "seating", "knapsack", "cleanser", "apparel",
         "device", "serpent", "scheme", "spectacles", "pullover",
         "joggers", "bed", "companions", "timepieces", "life science",
         "math", "luggage", "blades", "assassins", "hair wash"
         ]


chosen_word = rand.choice(words).lower()
# For debugging purposes
# print(chosen_word)

hang_man = (
    """
=====
|   |
|   ☺
| /-=-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""",
    """
=====
|   |
|   ☺
| /-=-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
    """
=====
|   |
|   ☺
| /-=-\ 
|   | 
|   | 
|  |
|
|
--------
""",
    """
=====
|   |
|   ☺
| /-=-\ 
|   | 
|   | 
|
|
|
--------
""",
    """
=====
|   |
|   ☺
| /-=-\ 
|   | 
|
|
|
|
--------
""",
    """
=====
|   |
|   ☺
| /-=-
|
|
|
|
|
--------
""",
    """
=====
|   |
|   ☺
|  -=-
|
|
|
|
|
--------
""",
    """
=====
|   |
|   ☺
|
|
|
|
|
|
--------
""",
    """
=====
|   |
|
|
|
|
|
|
|
--------
""")


unknown_word = []

# Display for unknown words
for letter in chosen_word:
    unknown_word.append("-")

# Player's desires
play_again = True

tries = len(hang_man) - 1

# For debugging
# print(f"You have {tries} tries")

print(hang_man[tries])
print(unknown_word)

while (tries != 0 and "-" in unknown_word):
    # Ask for input
    try:
        player_guess = str(input(">>> "))
    # Give error
    except:
        print("Invalid input it must be a string")
    # Exploring error cases
    else:
        if not player_guess.isalpha():
            print("This is not a letter please try again.")
        elif len(player_guess) > 1:
            print("This is not a valid guess.")
        elif player_guess in unknown_word:
            print("You have already guessed this letter.")
        else:
            # Go to next code block
            pass

    for i in range(len(chosen_word)):
        if player_guess == chosen_word[i]:
            unknown_word[i] = player_guess
            print(unknown_word)

    # Display Hangman State
    if player_guess not in unknown_word:
        tries -= 1
        print(hang_man[tries])
        print(unknown_word)

    # Ending State (Victory or Death)
    if "-" not in unknown_word:
        print("You won")
    elif tries == 0:
        print("You lost")
