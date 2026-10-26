import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.

    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def restart_game():
    yesno_input = ""
    while yesno_input != "Y" and yesno_input != "N":
        yesno_input = input("Would you like to play again? (Y/N)").capitalize()

    return yesno_input.capitalize() == "Y"

def play_game():

        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0

        print("Welcome to Snowman Meltdown!")

        while True:
            # For now, display the initial game state.
            display_game_state(mistakes, secret_word, guessed_letters)

            # Prompt user for one guess (logic to be enhanced later)
            guess = get_input()
            print("You guessed:", guess)

            if guess in secret_word:
                guessed_letters.append(guess)
            else:
                mistakes += 1
            if set (secret_word) == set (guessed_letters):
                print("You saved the Snowman and won!")
                if restart_game():
                    secret_word = get_random_word()
                    guessed_letters = []
                    mistakes = 0
                else:
                    return
            if mistakes >= len(ascii_art.STAGES):
                print("You lost!")
                if restart_game():
                    secret_word = get_random_word()
                    guessed_letters = []
                    mistakes = 0
                else:
                    return

def get_input( ):
    while True:
        guess = str(input("Guess a letter: ").lower())
        try:
            if len(guess) == 1 and guess not in ['0','1','2','3','4','5','6','7','8','9']:
                return guess
        except ValueError:
            pass
