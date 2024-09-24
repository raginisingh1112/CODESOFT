import random
import string

def generate_password(length):
    if length < 1:
        return "Length must be at least 1."

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase + uppercase + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("Password Generator!")
    while True:
        try:
            length = int(input("Enter required pass length: "))
            if length == 0:
                print("Exiting the application.")
                break
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()