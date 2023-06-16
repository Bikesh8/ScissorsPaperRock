import random

choices = ["scissors", "paper", "rock"]

while True:
    user_choice = input("Enter your choice (scissors, paper, rock): ").lower()
    computer_choice = random.choice(choices)
    
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "rock" and computer_choice == "scissors"):
        print("You win!")
    else:
        print("Computer wins!")
    
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thank you for playing")
        break
