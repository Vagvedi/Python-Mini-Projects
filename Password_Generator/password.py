import random
import string

def generate_password():
    print("\n🔐 PASSWORD GENERATOR PRO 🔐\n")

    try:
        length = int(input("Enter password length (min 6): "))
        if length < 6:
            print("❌ Password length should be at least 6.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == string.ascii_lowercase:
        print("❌ You must select at least one extra option.")
        return

    password = "".join(random.choice(characters) for _ in range(length))

    print("\n✅ Generated Password:")
    print(f"👉 {password}\n")

if __name__ == "__main__":
    generate_password()
