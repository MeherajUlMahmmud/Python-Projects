import random
import string
import argparse

def generate_password(length):
    # Define the characters to choose from for each category
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?~"

    # Create a pool of characters by combining all categories
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password by sampling from the pool
    password = random.choices(all_characters, k=length)

    # Convert the password list to a string
    password_str = ''.join(password)

    return password_str

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, help="Length of the password")

    args = parser.parse_args()

    # Generate a random password with the specified length
    random_password = generate_password(args.length)
    print("Random Password:", random_password)

if __name__ == "__main__":
    main()
