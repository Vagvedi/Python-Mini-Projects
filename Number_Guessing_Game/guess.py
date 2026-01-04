import random
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.CYAN + Style.BRIGHT + "\n🎯 NUMBER GUESSING GAME PRO 🎯")
    print(Fore.YELLOW + "Guess smart. Guess fast. Win clean.\n")

def choose_difficulty():
    print(Fore.MAGENTA + "Choose Difficulty:")
    print(Fore.GREEN + "1. Easy (1–50)")
    print(Fore.YELLOW + "2. Medium (1–100)")
    print(Fore.RED + "3. Hard (1–200)")

    while True:
        choice = input(Fore.CYAN + "Enter choice (1/2/3): ")
        if choice == "1":
            return 50
        elif choice == "2":
            return 100
        elif choice == "3":
            return 200
        else:
            print(Fore.RED + "Invalid choice. Try again.")

def play_game():
    banner()
    max_number = choose_difficulty()
    secret = random.randint(1, max_number)
    attempts = 0

    print(Fore.BLUE + f"\nI’m thinking of a number between 1 and {max_number} 👀")

    while True:
        guess = input(Fore.CYAN + "Your guess: ")

        if not guess.isdigit():
            print(Fore.RED + "⚠ Enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print(Fore.YELLOW + "📉 Too low!")
        elif guess > secret:
            print(Fore.YELLOW + "📈 Too high!")
        else:
            print(Fore.GREEN + Style.BRIGHT +
                  f"\n🏆 Correct! You guessed it in {attempts} attempts.")
            if attempts <= 5:
                print(Fore.GREEN + "🔥 INSANE performance!")
            elif attempts <= 10:
                print(Fore.CYAN + "👏 Solid guessing!")
            else:
                print(Fore.MAGENTA + "🙂 You got there!")
            break

if __name__ == "__main__":
    play_game()
