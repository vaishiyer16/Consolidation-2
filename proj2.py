import random
import pandas as pd
import matplotlib.pyplot as plt

# Function to simulate rolling three dice
def roll_dice():
    """Simulate rolling three dice."""
    return [random.randint(1, 6) for _ in range(2)]

# Function to check if the rolled dice constitute a 'tupled out' scenario
def is_tupled_out(dice):
    """Check if the rolled dice constitute a 'tupled out' scenario."""
    return len(set(dice)) == 1

# Function to fix dice with the same value
def fix_dice(dice):
    """Fix dice with the same value."""
    fixed_dice = []
    for die in dice:
        if dice.count(die) >= 2:
            fixed_dice.append(die)
        else:
            fixed_dice.append(None)
    return fixed_dice

# Main game function
def main():
    # Get input from the user for number of players and target score
    num_players = int(input("Enter the number of players: "))
    target_score = int(input("Enter the target score: "))
    
    # Initialize scores list for each player
    scores = [0] * num_players
    # Initialize list to store turn scores for each player
    turn_scores = [[] for _ in range(num_players)]

    # Loop until the maximum score reaches or exceeds the target score
    while max(scores) < target_score:
        for player in range(num_players):
            print(f"Player {player + 1}'s turn:")
            current_score = scores[player]
            dice = roll_dice()
            print("Dice:", dice)
            
            # Check for 'tupled out' scenario
            if is_tupled_out(dice):
                print("Tupled out! Score for this turn: 0")
                turn_scores[player].append(0)  # Record turn score
                continue
            
            # Fix dice with the same value
            fixed_dice = fix_dice(dice)
            print("Fixed dice:", fixed_dice)
            
            # Ask the player if they want to re-roll any dice
            while True:
                choice = input("Do you want to re-roll any dice? (y/n): ")
                if choice.lower() == 'n':
                    break
                elif choice.lower() == 'y':
                    indices = input("Enter indices of dice to re-roll (e.g., 0 2): ").split()
                    indices = [int(idx) for idx in indices if idx.isdigit() and int(idx) < 3]
                    for idx in indices:
                        dice[idx] = random.randint(1, 6)
                    print("New dice:", dice)
                    fixed_dice = fix_dice(dice)
                    print("Fixed dice:", fixed_dice)
            
            # Calculate score for this turn
            score = sum(d for d in dice if d is not None)
            print("Score for this turn:", score)
            # Update total score for the player
            scores[player] += score
            # Record turn score
            turn_scores[player].append(score)
            print("Total score:", scores[player])
            print()
            
            # If 'tupled out', reset player's score
            if is_tupled_out(dice):
                scores[player] = 0
                
            # Check if player wins
            if scores[player] >= target_score:
                print(f"Player {player + 1} wins!")
                break
    
    # Convert turn_scores to DataFrame
    df = pd.DataFrame(turn_scores).T
    df.columns = [f"Player {i+1}" for i in range(num_players)]
    
    # Plotting the scores
    plt.figure(figsize=(10, 6))
    df.plot(marker='o')
    plt.title("Player Scores Over Turns")
    plt.xlabel("Turn")
    plt.ylabel("Score")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

