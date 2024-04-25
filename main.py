# Allow random numbers to be taken
import random
# List of words for the game
hangman_words = ["computer", "chocolate", "jaguar", "zebra", "projector", "pencil"]

# Function that chooses a random word from the list.
def choose_word():
    return random.choice(hangman_words)

# Function that displays the hangman word with blanks for missing letters
def display_word(word, guessed_letters):
    displayed_word = ""
    # Iteration to repeat conditional statement
    for letter in word:
        # Conditional to check if letters guessed matches correct letters
        if(letter in guessed_letters):
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    # Return the word with correct guesses and blanks for unguessed letters
    return displayed_word

# Function that checks if the player has guessed all the letters
def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Function that starts the game
def play_hangman():
    chosen_word = choose_word()
    guessed_letters = []
    # Set amount of attempts
    attempts = 6

    # Intro to the game
    print("Welcome to Hangman!")
    print(f"You have {attempts} attempts to guess the word.")
    print(display_word(chosen_word, guessed_letters))

    # Keep the game running while user has attempts, end if they run out
    while(attempts>0):
        # Take input, convert to lowercase to prevent errors
        guess = input("Guess a letter: ").lower()

        # Check if the guess is composed of letters, and if so, a single letter
        if(len(guess) != 1 or not guess.isalpha()):
            print("Please enter a single letter.")
            # Forces the user to guess again
            continue

        # Check if the letter has already been guessed
        if(guess in guessed_letters):
            print("You've already guessed that letter.")
            #Forces the user to guess again
            continue

        # Add the letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is in the chosen word
        if(guess not in chosen_word):
            attempts -= 1;
            print(f"Incorrect! You have {attempts} attempts left.")
        else:
            print("Correct guess!")

        # Display the hangman word
        print(display_word(chosen_word, guessed_letters))

        # Check if the word has been guessed
        if(is_word_guessed(chosen_word, guessed_letters)):
            print(f"Congratulations! You guessed the word: {chosen_word}")
            break

        if(attempts==0):
          print(f"Sorry, out of attempts. The word was: {chosen_word}")

# Run the game!
play_hangman()
