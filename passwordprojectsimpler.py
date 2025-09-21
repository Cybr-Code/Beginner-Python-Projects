import random
import string
import sys


def get_yes_no(prompt):
    while True:
        choice = input(prompt + " (Y/N): ").strip().upper()
        if choice == "Y":
            return True
        elif choice == "N":
            return False
        else:
            print("Please enter Y or N.")


def get_password_length():
    while True:
        length = input("Enter password length (minimum 8): ")
        if length.isdigit() and int(length) >= 8:
            return int(length)
        else:
            print("Invalid input. Try again.")


def estimate_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%&*<>?" for c in password): score += 1
    if len(password) >= 12: score += 1

    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Excellent"]
    return levels[score]


def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    character_pools = []
    password_chars = []

    if use_lower:
        character_pools.append(string.ascii_lowercase)
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_upper:
        character_pools.append(string.ascii_uppercase)
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        character_pools.append(string.digits)
        password_chars.append(random.choice(string.digits))
    if use_symbols:
        symbol_set = "!@#$%&*<>?"
        character_pools.append(symbol_set)
        password_chars.append(random.choice(symbol_set))

    if not character_pools:
        print("You must select at least one character type.")
        sys.exit()

    all_chars = ''.join(character_pools)

    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)
    return ''.join(password_chars)


def main():
    print("🔐 Password Generator\n")

    while True:
        length = get_password_length()

        use_lower = get_yes_no("Include lowercase letters?")
        use_upper = get_yes_no("Include uppercase letters?")
        use_digits = get_yes_no("Include numbers?")
        use_symbols = get_yes_no("Include symbols?")

        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)

        print("\nGenerated Password:", password)
        print("Password Strength:", estimate_strength(password))

        again = get_yes_no("\nGenerate another password?")
        if not again:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()