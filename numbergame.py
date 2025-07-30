import random
def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")
number_guessing_game()
