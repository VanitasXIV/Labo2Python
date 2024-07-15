import random

def get_user_choice():
    """Get the user's choice."""
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    while True:
        user_input = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
        if user_input in choices:
            return user_input, choices[user_input]
        else:
            print("Invalid choice, please try again.")

def get_computer_choice():
    """Get the computer's choice."""
    choices = ['r', 'p', 's']
    computer_choice = random.choice(choices)
    choices_dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    return computer_choice, choices_dict[computer_choice]

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "You win!"
    else:
        return "You lose!"

def main():
    """Main function to run the game."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice, user_choice_name = get_user_choice()
        computer_choice, computer_choice_name = get_computer_choice()
        
        print(f"\nYou chose {user_choice_name}, computer chose {computer_choice_name}.\n")
        print(determine_winner(user_choice, computer_choice))

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
