import random

def get_user_choice():
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return "rock"
    elif choice == "2":
        return "paper"
    elif choice == "3":
        return "scissors"
    else:
        return None

def get_winner(user, computer):
    if user == computer:
        return "draw"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    print("\n🎮 ROCK PAPER SCISSORS PRO 🎮")

    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        user_choice = get_user_choice()

        if not user_choice:
            print("❌ Invalid choice. Try again.")
            continue

        computer_choice = random.choice(options)
        rounds += 1

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "draw":
            print("🤝 It's a draw!")
        elif winner == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        print(f"\n📊 Scoreboard after {rounds} rounds:")
        print(f"You: {user_score} | Computer: {computer_score}")

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            break

    print("\n🏁 Game Over")
    print(f"Final Score → You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing! 👋")

if __name__ == "__main__":
    play_game()
