import random

def number_guessing_game():
    print("🎯 Welcome to Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("❌ Please enter a valid number.\n")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.\n")
        elif guess > secret_number:
            print("📈 Too high! Try again.\n")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    number_guessing_game()
