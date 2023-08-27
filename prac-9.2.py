import random

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (0 for scissor, 1 for rock, 2 for paper): "))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ["Scissor", "Rock", "Paper"]
    computer_choice = random.randint(0, 2)
    
    user_choice = get_user_choice()
    
    print(f"You chose {choices[user_choice]}")
    print(f"Computer chose {choices[computer_choice]}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
