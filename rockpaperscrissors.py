def get_winner(player1_choice, player2_choice):
    # Define the winning rules
    winning_rules = {
        'rock': 'scissors',  # Rock beats scissors
        'scissors': 'paper',  # Scissors beats paper
        'paper': 'rock'  # Paper beats rock
    }
    
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif winning_rules[player1_choice] == player2_choice:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def main():
    valid_choices = ['rock', 'paper', 'scissors']
    
    # Get choices from both players
    player1_choice = input("Player 1, enter your choice (rock, paper, or scissors): ").lower()
    while player1_choice not in valid_choices:
        player1_choice = input("Invalid choice. Player 1, enter your choice (rock, paper, or scissors): ").lower()
    
    player2_choice = input("Player 2, enter your choice (rock, paper, or scissors): ").lower()
    while player2_choice not in valid_choices:
        player2_choice = input("Invalid choice. Player 2, enter your choice (rock, paper, or scissors): ").lower()
    
    # Determine the winner
    result = get_winner(player1_choice, player2_choice)
    print(result)

if __name__ == "__main__":
    main()
