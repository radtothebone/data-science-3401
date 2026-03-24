import random

# Grab a random number.
def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

# Ask the user for a guess.
def get_user_guess():
    while True:
        guess = input("Enter your guess: ")
        
        # Make sure it is actually a number.
        if guess.isdigit():
            return int(guess)
        else:
            print("Please enter a valid number.")

# See how bad the guess was.
def check_guess(guess, target):
    if guess < target:
        return "too low"
    elif guess > target:
        return "too high"
    else:
        return "correct"

# Main event.
def play_game():
    min_value = 1
    max_value = 100
    
    # Secret number.
    target = generate_random_number(min_value, max_value)
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {min_value} and {max_value}.")
    
    while True:
        # Get the user attempt.
        guess = get_user_guess()
        
        result = check_guess(guess, target)
        
        if result == "too low":
            print("Too low. Try again.")
        elif result == "too high":
            print("Too high. Try again.")
        else:
            print("Correct! You guessed the number.")
            break
        
        # In case they are tired of losing.
        stop = input("Do you want to keep playing? (yes/no): ").lower()
        
        if stop == "no":
            print("Game stopped.")
            break

# Start the game.
play_game()