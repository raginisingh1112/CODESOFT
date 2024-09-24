import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win!"
    else:
        return "lose!"

def main():
    user_score = 0
    computer_score = 0
    print(" Type 'exit' to quit the game.")

    while True:
        user_choice = input("Your choice: ").lower()
        
        if user_choice == 'exit':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f" You: {user_score}, Computer: {computer_score}")

        play_again = input("play again? (y/n): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()